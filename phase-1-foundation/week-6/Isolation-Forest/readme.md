## Isolation Forest

### What it is
Unsupervised anomaly detection — no labels involved. Outliers sit in sparse 
regions of feature space (not "can't be clustered," more precisely: far from 
dense clusters of normal points). That sparsity is exactly why random 
partitioning isolates them faster than normal points.

### Applications
Cybersecurity, fraud detection, healthcare (e.g. detecting unusual patient 
readings).

### How a tree is built
- Each tree is built on a random **subsample** of the data (default 256 
  points), not the full dataset. Smaller subsamples make outliers stand out 
  faster (too many points per tree causes "swamping/masking," where outliers 
  get buried).
- At every node, the tree picks a **random feature** and a **random split 
  value** between that feature's min and max. No optimization, unlike Week 5's 
  decision trees (which pick the *best* split). The randomness itself is what 
  makes rare/sparse points isolate quickly by chance.
- Tree grows until every leaf holds a single data point.

### Core assumption
If a point is an outlier, it gets isolated (reaches its own leaf) much 
earlier — i.e. at a shallower depth — than a normal point, because it has 
fewer "neighbors" nearby requiring extra splits to separate.

### E(h(x)) — per-point average path length across the forest
Computed separately for every point. For a single point x, look at what depth 
it got isolated at in each individual tree, then average those depths across 
all trees in the forest.

Example with 3 trees:
- Anomaly x isolated at depths [2, 3, 1] → E(h(x)) = 2.0
- Normal y isolated at depths [5, 6, 4] → E(h(y)) = 5.0

Anomalies get a small E(h(x)); normal points get a larger one.

### c(n) — normalization constant, NOT computed from your trees
c(n) depends only on n (subsample size) — a fixed theoretical formula (average 
path length of an unsuccessful search in a Binary Search Tree of n points):

c(n) = 2H(n-1) - (2(n-1)/n), where H(k) ≈ ln(k) + 0.5772

It exists purely to normalize E(h(x)) so the score lands between 0 and 1. 
Every point in the dataset is divided by the same c(n) — only E(h(·)) differs 
per point.

### Anomaly score formula
S(x,n) = 2^(-(E(h(x)) / c(n)))

- E(h(x)) << c(n) → S ≈ 1 → confidently an outlier
- E(h(x)) >> c(n) → S ≈ 0 → confidently normal
- E(h(x)) ≈ c(n) → S ≈ 0.5 → ambiguous
- Threshold on S decides the final outlier/normal cutoff.

### Remove vs. flag — a design decision, not automatic

Isolation Forest tells you a point is statistically rare. It does NOT tell you 
WHY — a genuine anomaly (fraud, rare disease pattern) and a data error (sensor 
glitch, typo) can get flagged identically. Deciding what to do next is a 
human/system-design decision, not something the model does for you.

**Remove entirely** — appropriate when the outlier is noise/error (e.g. 
age=999, corrupted sensor reading). No real signal is lost.

**Flag, don't remove** — appropriate when the anomaly IS the signal you care 
about (fraud, disease detection). Removing here would delete exactly what 
you're trying to find. Blind removal in critical domains (healthcare, fraud) 
can throw away the entire point of the system.

**How "flagging" actually works mechanically** — it's just adding an 
`is_anomaly` column to the data. Nothing automatically changes how downstream 
models treat that row; a few concrete patterns for what happens next:
1. The flag itself IS the output (e.g. fraud alert to a human reviewer — no 
   downstream model needed).
2. The flag becomes an extra input FEATURE for a downstream supervised model 
   (e.g. feed `is_anomaly` alongside other features into a Week-5-style tree 
   classifier).
3. The flag routes rows down different pipelines — normal points go through 
   the standard model, flagged points get pulled into a separate review queue 
   or specialized handling.

Isolation Forest's job ends at detection. Everything after (remove, route, 
feed as feature) is a separate design decision depending on domain and what 
the anomaly actually represents.