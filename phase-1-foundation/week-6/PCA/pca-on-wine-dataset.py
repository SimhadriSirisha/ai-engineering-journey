import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

scaler = StandardScaler()
X = scaler.fit_transform(df)

pca = PCA(n_components=2)
pca.fit(X)

print(f'features transformed :{pca.get_feature_names_out()}')
print(f'Total variance captured: {pca.explained_variance_ratio_.sum():.3f}') # how much of the total spread/information across all 13 features is preserved in 2D.

X_new = pca.transform(X)

km = KMeans(n_clusters=3, n_init=10, random_state=42)
cluster_labels = km.fit_predict(X_new)

real_labels = data.target  # the actual wine types, 0/1/2

score = adjusted_rand_score(real_labels, cluster_labels)
print("agreement score:", score)

loadings = pd.DataFrame(
    pca.components_.T,  # transpose so rows = original features
    columns=['PC1', 'PC2'],
    index=data.feature_names
)

print(loadings.sort_values('PC1', ascending=False))