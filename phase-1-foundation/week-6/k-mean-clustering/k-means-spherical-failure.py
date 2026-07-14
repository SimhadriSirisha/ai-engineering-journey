from sklearn.datasets import make_moons
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

km = KMeans(n_clusters=2, n_init=10, random_state=42)
labels = km.fit_predict(X_moons)

plt.scatter(X_moons[:, 0], X_moons[:, 1], c=labels, cmap='tab10')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], c='black', marker='X', s=200)
plt.title('K-Means on two crescent moons')
plt.show()