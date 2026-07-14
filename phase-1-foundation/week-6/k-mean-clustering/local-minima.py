from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


X_blob, _ = make_blobs(n_samples=300, centers=6, cluster_std=1.5, random_state=1)

fig, axes = plt.subplots(2, 5, figsize=(20, 8))
axes = axes.flatten()

inertias = []
for i, seed in enumerate(range(10)):
    km = KMeans(n_clusters=6, n_init=1, random_state=seed)  # n_init=1 is the key — forces bad luck
    labels = km.fit_predict(X_blob)
    inertias.append(km.inertia_)

    axes[i].scatter(X_blob[:, 0], X_blob[:, 1], c=labels, cmap='tab10', s=15)
    axes[i].scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], 
                     c='black', marker='X', s=100)
    axes[i].set_title(f'seed={seed}\ninertia={km.inertia_:.1f}')
    axes[i].set_xticks([])
    axes[i].set_yticks([])

plt.tight_layout()
plt.show()

print("inertias:", inertias)
print("min:", min(inertias), "max:", max(inertias))