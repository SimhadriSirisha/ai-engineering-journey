from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
import pandas as pd

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

X = df[['alcohol', 'color_intensity']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia_values = []

for k in range(1,8):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit_predict(X_scaled)
    inertia = km.inertia_ # cost 
    inertia_values.append(inertia)
    print(f"k: {k} : inertia: {inertia}")

plt.plot(range(1, 8), inertia_values, marker='o')
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()

km3 = KMeans(n_clusters=3, n_init=10, random_state=42)
cluster_labels = km3.fit_predict(X_scaled)

real_labels = data.target  # the actual wine types, 0/1/2

score = adjusted_rand_score(real_labels, cluster_labels)
print("agreement score:", score)

# notes : elbow method narrows the range, it doesn't hand you a single correct K.