import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from joblib import dump, load

df = pd.read_csv("Housing.csv")

# --- Encoding Yes/No Columns ---
binary_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
df[binary_cols] = df[binary_cols].replace({'yes': 1, 'no': 0})

# --- Encoding Furnishing Status ---
furnishing_status_mapping = {'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2}
df['furnishingstatus'] = df['furnishingstatus'].replace(furnishing_status_mapping)

# Shuffling the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split the data into features and target
X = df.drop(columns=['price'])
print(X.dtypes)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regModel = LinearRegression().fit(X_train, y_train)
print(regModel.score(X_train, y_train))
print(regModel.score(X_test, y_test))

print("-------------------------")

# comparision with dummy regressor

dump(regModel, "house-pricing-model.pkl")

# to verify it saved/loads correctly:
loaded_model = load("house-pricing-model.pkl")
print(X_test[:5])
print(loaded_model.predict(X_test[:5]))
print(regModel.predict(X_test[:5]))  # compare — should be identical