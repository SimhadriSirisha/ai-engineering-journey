from matplotlib.typing import MarkerType
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

# inject 5 synthetic outliers - extreme values far outside normal range
outliers = pd.DataFrame({
    col: np.random.uniform(df[col].min()*3, df[col].max()*3, 5)
    for col in df.columns
})

df_combined = pd.concat([df, outliers], ignore_index=True)
labels_true = np.array([1]*len(df) + [-1]*len(outliers))  # 1=normal, -1=injected outlier

scaler = StandardScaler()
X = scaler.fit_transform(df_combined)

iso = IsolationForest(n_estimators=100, contamination=0.03, random_state=42)
preds = iso.fit_predict(X)  # returns 1 (normal) or -1 (anomaly)
scores = iso.decision_function(X)  # higher = more normal, lower = more anomalous

print("Predictions for injected outliers:", preds[-5:])
print("Scores for injected outliers:", scores[-5:])
print("Predictions for last 5 real wines:", preds[len(df)-5:len(df)])

indx = np.where(preds < 0)

# PCA fit to combine data (outliers included
pca_after = PCA(n_components=2)
X_2d = pca_after.fit_transform(X)

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

axes[0].scatter(X_2d[:, 0], X_2d[:, 1], c='steelblue', s=20, label = 'real wine with outliers')
axes[0].legend()

axes[1].scatter(X_2d[:, 0], X_2d[:, 1], c='steelblue', s=25)
axes[1].scatter(X_2d[indx,0], X_2d[indx, 1], edgecolors = "r", facecolors='none', s=60, label = 'Outliers identified')
axes[1].legend() 

plt.tight_layout()
plt.show()