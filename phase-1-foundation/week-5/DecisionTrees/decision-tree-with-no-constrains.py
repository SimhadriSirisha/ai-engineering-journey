import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.tree import plot_tree

print(os.getcwd())

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'breast-cancer-data-cleaned.csv')
df = pd.read_csv(file_path)

# Split the data into features and target
X = df.drop(columns=['diagnosis'])
y = df['diagnosis']

# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

# Predict the test set
y_pred = tree.predict(X_test)

# Confusion matrix

cf_matrix = confusion_matrix(y_test, y_pred)
print(cf_matrix)
sensitivity = cf_matrix[1,1] / (cf_matrix[1,1] + cf_matrix[1,0])
specificity = cf_matrix[0,0] / (cf_matrix[0,0] + cf_matrix[0,1])
print(sensitivity)
print(specificity)

cm_train = confusion_matrix(y_train, tree.predict(X_train))
cm_test  = confusion_matrix(y_test, y_pred)
print("Train CM:\n", cm_train)
print("Test CM:\n", cm_test)

# ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
# plt.show()

# accuracy score
accuracy = accuracy_score(y_test, y_pred, normalize=False)
print("accuracy:", accuracy)

train_accuracy = tree.score(X_train, y_train)
print("train_accuracy:", train_accuracy)

test_accuracy = tree.score(X_test, y_test)
print("test_accuracy:", test_accuracy)

report = classification_report(y_test, y_pred)
print("classification_report:\n", report)

plt.figure(figsize=(20,10))
plot_tree(tree, filled=True, feature_names=X.columns, class_names=['M', 'B'])
plt.show()