```markdown
## PCA (Principal Component Analysis)

### What it is
PCA is fully unsupervised — it has no concept of a target/label or "the model." 
It only looks at variance/spread within the feature space itself. It finds new 
axes (directions) along which the data varies the most, using only the features 
themselves.

This is fundamentally different from feature selection, which drops features 
based on how useful they are for predicting a target. PCA doesn't know what 
"useful for prediction" even means — a feature with huge variance but zero 
predictive power gets kept; a feature that's the best predictor but has tiny 
variance can get discarded.

### Centering — the required first step
PCA subtracts the mean of each feature before doing anything else. This removes 
the data's absolute position in space, leaving only the true relative spread 
between points.

Without centering, PCA's answer gets dominated by wherever the data happens to 
sit (e.g. if all values are far from zero), not by the actual shape/spread of 
the data — a technically-computable but meaningless result, with no error thrown. 
This is a silent failure mode.

`sklearn.decomposition.PCA()` centers automatically — no manual step needed. 
Can verify via `pca.mean_` after fitting.

### How a principal component is found
- PC1 = the direction (after centering) along which projected points have 
  maximum variance. Equivalently: the direction that minimizes squared 
  reconstruction distance from each point to its projection. Same objective, 
  two ways of stating it.
- Every subsequent PC (PC2, PC3, ...) must be orthogonal (perpendicular) to all 
  previous PCs, while still capturing the most remaining variance. This 
  orthogonality constraint is why PCA gives one unique answer, not an 
  arbitrary one.
- Each PC is a linear combination of ALL original features (e.g. 
  PC1 = 0.6×alcohol + 0.3×color_intensity + 0.1×flavanoids + ...) — not a 
  subset of original columns. "Keeping 2 PCs" ≠ "keeping 2 original features."

### Eigenvalues vs singular values
- Classic approach: compute the covariance matrix, find its eigenvector/
  eigenvalue pairs. Each eigenvector = a PC (direction); its eigenvalue = how 
  much variance lies along that direction. Always come as a pair — an 
  eigenvector without its eigenvalue is meaningless here.
- sklearn's `PCA` actually uses SVD (singular value decomposition) internally 
  for numerical stability, not direct eigendecomposition. Same answer either 
  way — they're mathematically linked: `eigenvalue = (singular value)² / 
  (n_samples - 1)`.

### How many PCs to keep — scree plot / explained variance
- Scree plot: plot eigenvalue (or explained variance) per PC, ranked largest 
  to smallest. Pick the top N that capture "enough" variance.
- Never trust a 2D PCA plot blindly — always check the explained variance 
  ratio for the PCs you kept (e.g. `pca.explained_variance_ratio_`). If PC1+PC2 
  only explain 40% of total variance, conclusions drawn from that 2D plot are 
  built on a shaky foundation. If they explain 85%+, much more trustworthy.

### Max number of PCs
Max possible PCs = `min(n_samples - 1, n_features)`, not `min(n_samples, 
n_features)`. The "-1" comes from centering: after subtracting the mean, all 
centered points are constrained to sum to zero — one linear constraint, which 
caps the achievable rank at `n_samples - 1` regardless of feature count. This 
only matters when samples are scarce relative to features (e.g. 2 samples, 5 
features → max 1 usable PC). Irrelevant for datasets like wine (178 samples, 
13 features) where samples vastly outnumber features.

Actual usable PCs can be fewer still if features are linearly dependent 
(redundant/duplicate information) — those directions carry zero variance and 
produce eigenvalues of ~0.

### Failure mode to test
Compare adjusted_rand_score of clusters built on 2 arbitrarily-picked features 
vs. clusters built on 2 PCs derived from ALL features. Arbitrary 2-feature 
selection has a hard ceiling — it can't reconstruct signal that lives in the 
other unused features. PCA compresses info from all features into the 2 kept 
dimensions, so it should recover more of the true structure.
```

### Experiment: 2 arbitrary features vs 2 PCA components (wine dataset)

Setup: compared K-Means clustering agreement (adjusted_rand_score against real 
wine cultivar labels) using three feature sets:

| Feature set | Variance captured | Adjusted Rand Score |
|---|---|---|
| 2 arbitrary raw features (alcohol, color_intensity) | n/a | 0.535 |
| 2 PCA components (from all 13 features) | 55.4% | 0.895 |
| All 13 PCA components (full rotation, no reduction) | 100% | 0.895 |

**Why 2 raw features underperformed:** picking 2 columns arbitrarily throws 
away information in the other 11 — the real wine classes were originally 
defined using the full chemical profile, so 2 arbitrary features have a hard 
ceiling on how well they can reconstruct that structure.

**Why 2 PCA components did much better:** each PC is a linear combination of 
ALL 13 original features, so even a 2D projection carries compressed signal 
from every feature, not just 2 of them.

**Why 55% variance retained still gave full (100%-PC) agreement:** explained 
variance and clustering agreement answer different questions. Explained 
variance = how much of the total spread across all features survives 
compression. ARI = how well that space happens to separate the classes we 
care about. Here, PC3–PC13 (the other 45% of variance) added zero additional 
separating power for wine cultivar clustering — confirmed by all-13-PCs giving 
the identical 0.895 score as just 2 PCs. The discriminative structure was 
concentrated entirely in the top 2 directions; the remaining variance was 
mostly noise irrelevant to this particular clustering task. This won't always 
be true — it happened here because the true classes are strongly aligned with 
the highest-variance directions in this dataset.

**my original 2 features approximated PC2 but completely missed PC1, which happened to be the stronger signal."**

### PCA loadings — what actually drives the top components (wine dataset)

| PC | Top drivers (by magnitude) |
|---|---|
| PC1 | flavanoids (0.42), total_phenols (0.39), od280/od315 (0.38) |
| PC2 | color_intensity (-0.53), alcohol (-0.48), proline (-0.36) |

**Unexpected finding:** PC1 — the single largest source of variance in the 
whole dataset — is driven by phenolic chemistry (flavanoids, phenols), not by 
alcohol or color, which is what business intuition would have guessed first. 
My original 2-feature choice (alcohol + color_intensity) turned out to 
approximate PC2's territory, but completely missed PC1. This directly 
explains the earlier 0.535 → 0.895 jump: I wasn't picking bad features, I was 
missing the dominant signal in the dataset entirely.

### Scree plot + cumulative variance

- Scree plot (variance per individual PC): steep drop from PC1 (36%) → PC2 
  (19%) → PC3 (11%), then flattens — classic elbow shape, same concept as the 
  K-Means inertia elbow, applied to variance instead.
- Cumulative variance: takes **7 components to cross 90%** of total variance. 
  PC1+PC2 alone only reach ~55%.

**Key lesson — "how many PCs to keep" has no single universal answer, it 
depends on the task:**
- Goal = faithfully reconstruct/preserve the original data → need 7+ PCs 
  (90% variance threshold).
- Goal = separate the 3 known wine cultivars via clustering → 2 PCs were 
  enough, and going all the way to 13 PCs (100% variance) gave the *identical* 
  clustering score (0.895). The class-discriminating signal happened to 
  concentrate entirely in the top 2 directions.

Scree/cumulative variance answers "how much information is preserved." It 
does NOT answer "how well does this serve my specific downstream task" — 
those can point to different numbers of components entirely.

### PCA — closing summary
- Fully unsupervised, no target/label involved — operates only on feature 
  variance.
- Centering (subtract mean) is mandatory and automatic in sklearn; without 
  it, PCA is dominated by the data's absolute position, not its shape.
- Each PC is a linear combination of ALL original features, not a subset — 
  "PCA feature selection" is a contradiction in terms.
- Max components = min(n_samples - 1, n_features); fewer still if features 
  are linearly dependent (eigenvalue ≈ 0).
- Explained variance retained ≠ task performance — always check both 
  independently rather than assuming one implies the other.