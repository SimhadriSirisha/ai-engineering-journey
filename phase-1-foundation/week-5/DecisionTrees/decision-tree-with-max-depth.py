import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

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
max_depths = [2, 3, 5, 10, None]
train_accuracies = []
test_accuracies = []
for max_depth in max_depths:    
    tree = DecisionTreeClassifier(max_depth=max_depth)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    print(f"Max Depth: {max_depth}, Accuracy: {accuracy_score(y_test, y_pred)}")
    train_accuracy = tree.score(X_train, y_train)
    train_accuracies.append(train_accuracy)
    test_accuracy = tree.score(X_test, y_test)
    test_accuracies.append(test_accuracy)
    print("--------------------------------")

print(f"Train accuracies: {train_accuracies}")
print(f"Test accuracies: {test_accuracies}")

plt.plot(max_depths, train_accuracies, label='Train Accuracy')
plt.plot(max_depths, test_accuracies, label='Test Accuracy')
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.title('Max Depth vs Accuracy')
plt.legend()
plt.show()