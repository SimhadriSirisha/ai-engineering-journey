## Week 4 revisit: Linear Regression (sklearn) — dockerization prep

Redid Week 4's from-scratch linear regression using sklearn, in preparation 
for saving/serving the model via Docker + FastAPI.

### Bug 1: trained on full X, scored on split data
Original code did `.fit(X, y)` (entire dataset) but then scored on 
`X_train`/`X_test` from a separate split. This means the "test" score wasn't 
measuring generalization at all — the model had already seen those rows 
during training. Fix: always `.fit()` only on `X_train`.

### Bug 2: trained on unscaled X, scored on scaled X_train/X_test
Introduced `StandardScaler` but only used it to build `X_train`/`X_test` — 
the model itself was still fit on raw unscaled `X`. Feeding scaled inputs to 
a model trained on raw-magnitude inputs produced a badly negative R² score, 
since the learned coefficients didn't match the input scale being tested. 
Lesson: train and evaluate must always use the exact same preprocessing 
pipeline, consistently.

### Does Linear Regression need feature scaling?
Tested directly: scaled vs. unscaled features gave identical R² once the two 
bugs above were fixed. This makes sense — plain Linear Regression has a 
closed-form solution that adjusts each coefficient's magnitude to exactly 
compensate for that feature's scale, so final predictions/score are 
scale-invariant. This is fundamentally different from K-Means or PCA, which 
are distance/variance-based and DO require scaling.

Where scaling would start to matter: Ridge/Lasso regularization, since the 
penalty term applies directly to coefficient magnitude — an unscaled 
large-magnitude feature gets penalized unfairly vs. a small-scale one.

Decision: dropped the scaler from the final pipeline entirely, since it adds 
no value here and keeps the saved model/Docker image simpler.

### Final model performance
- Train R²: 0.68 | Test R²: 0.66 — small, healthy train/test gap, no 
  overfitting signal.
- Baseline check: `DummyRegressor(strategy='mean')` scores ~0.0 on train and 
  test (predicts the average price for every row, explains zero variance by 
  definition).
- Honest framing: the model explains ~66-68 percentage points of price 
  variance beyond a naive "always guess the average" baseline, using only 12 
  basic structural features (no location, condition, or market data 
  available in this dataset). Context matters more than the raw R² number in 
  isolation.

## Model persistence — choosing joblib

### Decision path (sklearn's own guidance)
1. **Need the Python object back, or just predictions?** Only predictions → 
   ONNX is a valid option (cross-language, no Python/sklearn needed at 
   inference). Need the object (`.coef_`, `.predict()`, further Python work) 
   → pickle/joblib family.
2. **Trust the source of the model file?** pickle/joblib both execute 
   arbitrary code on load (security risk if the file's source isn't trusted) 
   — use `skops.io` if that's a concern. Since I train, save, and load the 
   model myself in my own pipeline, full trust chain — this risk doesn't 
   apply here.
3. **Care about load performance / memory-mapped sharing across processes?** 
   Yes → joblib. No → plain pickle is sufficient.

**My case:** staying entirely in Python, staying in FastAPI, training and 
loading the file myself. ONNX technically fits step 1 (only need 
predictions), but adds real costs not worth it for a small model + 
beginner-friendly pipeline: extra conversion step (`skl2onnx`), one more 
library that can silently break, harder to debug (can't just inspect 
`.coef_` directly in a Python shell). Chose joblib for simplicity and 
debuggability over ONNX's cross-language benefit, which I don't need.

### Why joblib over plain pickle
joblib is optimized specifically for objects containing large NumPy arrays — 
exactly what a fitted sklearn model is (`.coef_`, `.intercept_` are NumPy 
arrays). Benefits:
- More efficient serialization of NumPy-heavy objects than plain pickle.
- Supports memory-mapping (`mmap_mode`) for fast, shared loading across 
  multiple processes — relevant when an API serves many requests, though 
  overkill for a small model like this one.
- `joblib.dump()` takes a filename directly and manages file I/O internally 
  — don't wrap it in a manual `open()`, that bypasses part of what makes it 
  efficient.

### Mistakes caught while saving
- Used `open(..., "wb")` + `dump(..., protocol=5)` manually — unnecessary; 
  `joblib.dump(model, "filename.pkl")` handles file I/O itself.
- Misunderstood `mmap_mode='r+'` as read-only — it's actually **read+write** 
  (same convention as Python's `open()`: `'r'`=read-only, `'r+'`=read-write). 
  For a model you only ever `.predict()` with, never modify, the correct mode 
  is `'r'` or to omit `mmap_mode` entirely — memory-mapping only pays off for 
  large arrays reused across many processes, not a small regression model.
- `protocol=5` supports out-of-band buffers for large binary data — real 
  benefit for large NumPy arrays (e.g. deep learning weights), negligible 
  for this small model (12 coefficients).
- **Verification step that matters:** always confirm `load()` gives 
  identical `.predict()` output to the original in-memory model on the same 
  input rows — saving without confirming reload correctness is only half done.


## Trade-off in reducing the docker image size

"Reduced the image from 709MB to 596MB by removing pandas (replaced DataFrame construction with a plain ordered list matching the model's trained feature order). The remaining size is dominated by scikit-learn and its scipy dependency — compiled numerical libraries, not removable without reimplementing prediction logic by hand, which would tightly couple the API to one specific model type and break on retraining with a different algorithm. Chose to keep scikit-learn intact for maintainability over squeezing further size reduction."