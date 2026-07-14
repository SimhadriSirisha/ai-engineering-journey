### What K-Means actually is
K-Means is NOT a one-shot calculation like matrix multiplication — it's an iterative 
fixed-point algorithm: guess centroids → assign points → recompute centroids → repeat 
until inertia stops decreasing. Closer to PageRank/EM convergence than to a typical 
single-pass Spark job.

### Scaling — concrete example, not just theory
Tested on wine dataset: alcohol (std=0.81) vs color_intensity (std=2.32) — a ~3x 
difference in spread. Unscaled K-Means centroids barely varied on alcohol at all 
(2.8, 5.2, 8.8 spread only on color_intensity) — meaning the higher-variance feature 
silently dominated the distance calculation and alcohol was effectively ignored. 
After StandardScaler, both features contributed and clusters followed the actual 
diagonal trend in the data. No error was thrown either way — this is a silent bug, 
not a crash.

### random_state — what it actually controls
random_state seeds the INITIAL centroid placement only. Once centroids are placed, 
point assignment is deterministic (nearest centroid, by calculation). Different seeds 
→ different starting points → can converge to different local minima. This is why 
local minima is possible at all despite K-Means always moving "downhill."

### Feature choice matters as much as K
Clustered wine data on just 2 of 13 available features (alcohol, color_intensity), 
then checked agreement against real wine cultivar labels using adjusted_rand_score: 
got 0.535 (1.0 = perfect, 0.0 = random). Real wine categories were defined using all 
13 chemical features — asking 2 features to reconstruct a label built from 13 has a 
hard ceiling. Not a K or scaling problem — a feature-selection limitation.

### Inertia
- inertia means its a sum of squared distance between centroid and data point. Basically its a cost. We try to reduce the inertia by slowly moving the cluster centroid to ri8 place.

### failures of K-means
1. How to select k ? we have ELBOW method where we find what is the inertia for different no of clusters. Why its called elbow because it will do steep drop at first and then steadily decreases. But this is not reliable algorithm because as we increse k, inertia continuously decreases. so k basically choosem wrt bussiness needs.
2. K-Means can't correctly separate clusters that are curved or non-convex (e.g. moon shapes) — it can only draw straight-line boundaries between centroids (Voronoi regions).
    - K-Means assumes clusters are convex, roughly circular blobs of similar size.
     Any time our real clusters are elongated, curved, or nested inside each other,
     K-Means will produce a confident, clean-looking answer that is structurally wrong — and there's no error or warning, 
     it just silently gives us the wrong grouping. This is a strong Friday failure-post candidate: "K-Means was 100% confident and 100% wrong" 
3. There will be different local-minimas (min inertia) for different initialization of cluster centroids.
    - that's y we have n-init, a interger which tells the model to do clustering n-init time and get me the centroids with min inertial.
    - This only holds when comparing different seeds at the same K. we can't use inertia to compare across different K values — inertia mechanically decreases as K increases regardless of quality.
    - In our day-to-day work, we'll rarely see this problem directly, because n_init=10 (sklearn's current default) hides it from us. we only saw it because we deliberately forced n_init=1. This is the "silent failure protection" point from earlier — the library quietly does the right thing by default, and it's worth knowing why, in case we ever inherit code where someone set n_init=1 without realizing the risk.