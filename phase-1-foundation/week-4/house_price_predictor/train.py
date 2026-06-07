import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Housing.csv")

# --- Encoding Yes/No Columns ---
binary_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
df[binary_cols] = df[binary_cols].replace({'yes': 1, 'no': 0})

# --- Encoding Furnishing Status ---
furnishing_status_mapping = {'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2}
df['furnishingstatus'] = df['furnishingstatus'].replace(furnishing_status_mapping)

print("encoded data:\n", df.head())
print(df.dtypes)

# Shuffling the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# --- Splitting Data ---
split = int(0.8 * len(df))
train_df = df[:split]
test_df  = df[split:]

# Compute scaling stats from TRAIN only
mu    = np.mean(train_df, axis=0)
sigma = np.std(train_df, axis=0)

# Apply to both
train_scaled = (train_df - mu) / sigma
test_scaled  = (test_df  - mu) / sigma

print("any null values in scaled data:\n", train_scaled.isnull().values.any())
print("any null values in test scaled data:\n", test_scaled.isnull().values.any())

# --- Seperating X & Y ---
train_X = train_scaled.drop('price', axis=1).values
train_y = train_scaled['price'].values
test_X  = test_scaled.drop('price', axis=1).values
test_y  = test_scaled['price'].values

print("train_X shape:\n", train_X.shape)
print("train_y shape:\n", train_y.shape)
print("test_X shape:\n", test_X.shape)
print("test_y shape:\n", test_y.shape)

# --- Training the model ---
W = np.zeros(train_X.shape[1])
b = 0

learning_rate = 0.01
iterations = 2000

# --- model function ---
def model(W, b, X):
    return np.dot(W, X) + b

# --- cost function ---
def cost_function(W, b, X, Y):
    Y_pred = X @ W + b
    return np.mean((Y_pred - Y) ** 2) / 2

# --- gradient descent W derivative ---
def get_gradients(W, b, X, Y):
    Y_pred = X @ W + b          # (436,)
    error  = Y_pred - Y         # (436,)
    dW     = (X.T @ error) / len(X)   # (12,) — one gradient per weight
    db     = np.mean(error)            # scalar
    return dW, db


def gradient_descent(W, b, X, Y, learning_rate, iterations):
    costs = []
    for i in range(iterations):
        dW, db = get_gradients(W, b, X, Y)
        W = W - learning_rate * dW
        b = b - learning_rate * db
        cost = cost_function(W, b, X, Y)
        costs.append(cost)
        if i % 100 == 0:
            print(f"Iteration {i}, Cost: {cost:.6f}")
    return W, b, costs

# --- training the model ---
W, b, cost = gradient_descent(W, b, train_X, train_y, learning_rate, iterations)

features = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
            'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
            'parking', 'prefarea', 'furnishingstatus']

for f, w in zip(features, W):
    print(f"{f:20s} : {w:.4f}")


# --- Evaluation ---
y_pred_train = train_X @ W + b
y_pred_test  = test_X  @ W + b

# MSE
train_mse = np.mean((y_pred_train - train_y) ** 2)
test_mse  = np.mean((y_pred_test  - test_y)  ** 2)

# R² score — how much variance your model explains
def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

train_r2 = r2_score(train_y, y_pred_train)
test_r2  = r2_score(test_y,  y_pred_test)

print(f"Train MSE: {train_mse:.4f} | Test MSE: {test_mse:.4f}")
print(f"Train R²:  {train_r2:.4f} | Test R²:  {test_r2:.4f}")

features = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
            'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
            'parking', 'prefarea', 'furnishingstatus']

# Sort by absolute weight value
importance = sorted(zip(features, W), key=lambda x: abs(x[1]), reverse=True)

print("Feature Importance:")
for feature, weight in importance:
    print(f"{feature:20s} : {weight:.4f}")