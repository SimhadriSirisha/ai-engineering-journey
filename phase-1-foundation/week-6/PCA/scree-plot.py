import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

scaler = StandardScaler()
X = scaler.fit_transform(df)

pca_full = PCA()
pca_full.fit(X)

plt.figure(figsize=(8,5))
plt.plot(range(1, len(pca_full.explained_variance_ratio_)+1), 
         pca_full.explained_variance_ratio_, marker='o')
plt.xlabel('Principal Component')
plt.ylabel('Explained variance ratio')
plt.title('Scree plot - wine dataset')
plt.show()

# cumulative version - often more useful for deciding cutoff
plt.plot(range(1, len(pca_full.explained_variance_ratio_)+1), 
          pca_full.explained_variance_ratio_.cumsum(), marker='o')
plt.axhline(y=0.9, color='r', linestyle='--', label='90% threshold')
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.legend()
plt.show()