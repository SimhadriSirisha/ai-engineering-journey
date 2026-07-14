from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

X = df[['alcohol', 'color_intensity']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


km_unscaled = KMeans(n_clusters=3, n_init=10, random_state=42)
labels_unscaled = km_unscaled.fit_predict(X)  # raw X, not X_scaled

km_scaled = KMeans(n_clusters=3, n_init=10, random_state=42)
labels_scaled = km_scaled.fit_predict(X_scaled)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(X['alcohol'], X['color_intensity'], c=labels_unscaled, cmap='tab10')
axes[0].set_title('Unscaled')
axes[0].set_xlabel('alcohol')
axes[0].set_ylabel('color_intensity')
axes[1].scatter(X['alcohol'], X['color_intensity'], c=labels_scaled, cmap='tab10')
axes[1].set_title('Scaled')
axes[1].set_title('Unscaled')
axes[1].set_xlabel('alcohol')
plt.show()

# print('inertia:', km.inertia_)