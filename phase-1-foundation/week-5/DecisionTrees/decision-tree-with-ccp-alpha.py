import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print(os.getcwd())

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'breast-cancer-data-cleaned.csv')
df = pd.read_csv(file_path)

# Split the data into features and target
X = df.drop(columns=['diagnosis'])
y = df['diagnosis']

# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model
tree = DecisionTreeClassifier(random_state=0)
path = tree.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities


trees = []
for ccp_alpha in ccp_alphas:
    tree = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    tree.fit(X_train, y_train)
    trees.append(tree)

train_scores = [tree.score(X_train, y_train) for tree in trees]
test_scores = [clf.score(X_test, y_test) for clf in trees]

fig, ax = plt.subplots(1,2)
ax[0].plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax[0].set_xlabel("effective alpha")
ax[0].set_ylabel("total impurity of leaves")
ax[0].set_title("Total Impurity vs effective alpha for training set")

ax[1].set_xlabel("alpha")
ax[1].set_ylabel("accuracy")
ax[1].set_title("Accuracy vs alpha for training and testing sets")
ax[1].plot(ccp_alphas, train_scores, marker="o", label="train", drawstyle="steps-post")
ax[1].plot(ccp_alphas, test_scores, marker="o", label="test", drawstyle="steps-post")
ax[1].legend()
fig.tight_layout()
plt.show()
