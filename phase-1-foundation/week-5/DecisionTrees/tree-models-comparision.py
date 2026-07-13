import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'breast-cancer-data-cleaned.csv')
df = pd.read_csv(file_path)

# Split the data into features and target
X = df.drop(columns=['diagnosis'])
y = df['diagnosis']

# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Decision Tree (ccp_alpha=0.014)": DecisionTreeClassifier(ccp_alpha=0.014, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(random_state=42, eval_metric='logloss')
}

for name, model in models.items():
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    print(f"{name}: Train={train_acc:.4f}, Test={test_acc:.4f}")