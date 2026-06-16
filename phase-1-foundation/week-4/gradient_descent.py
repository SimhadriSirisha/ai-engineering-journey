import numpy as np
import matplotlib.pyplot as plt

# --- Data ---
x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
y_train = np.array([250, 300, 480,  430, 630, 730,])
m = len(x_train)

# --- Model ---
def model(w, x, b):
    return w*x + b

# --- Cost function (MSE) ---
def cost_func(w, b):
    squared_error_value = 0
    for i in range(0,m):
        pred_value = model(w, x_train[i], b)
        squared_error_value += (pred_value - y_train[i]) ** 2

    return (1/(2*m))*squared_error_value

# --- Gradients ---
def get_w_derivative(w, b):
    result = 0
    for i in range(0, 6):
        pred_value = model(w, x_train[i], b)
        result += ((pred_value - y_train[i])*x_train[i])
    return (1/m) * result

def get_b_derivative(w, b):
    result = 0
    for i in range(0, m):
        pred_value = model(w, x_train[i], b)
        result += (pred_value - y_train[i])
    return (1/m) * result

# --- Gradient Descent ---
def gradient_descent(w, b, learning_rate, iterations):
    w_vals = []
    b_vals = []
    costs =  []

    temp_w = 0
    temp_b = 0

    for _ in range(iterations):
        w_derivative = get_w_derivative(w, b)
        b_derivative = get_b_derivative(w, b)
        
        w -= learning_rate * w_derivative
        b -= learning_rate * b_derivative
        cost = cost_func(w, b)

        w_vals.append(w)
        b_vals.append(b)
        costs.append(cost)

    return w, b, w_vals, b_vals, costs

# --- Run ---
w_final, b_final, w_vals, b_vals, costs = gradient_descent(w=10, b=5, learning_rate=0.01, iterations=10000)

# --- Predictions ---
preds = [model(w_final, x, b_final) for x in x_train]

print(f"Final w: {w_final:.2f}, Final b: {b_final:.2f}")
print(f"Final cost: {costs[-1]:.2f}")


fig, axes = plt.subplots(2, 3, figsize=(16, 8))
fig.suptitle("Gradient Descent — Linear Regression", fontsize=14)

# Plot 1: Data + fitted line
axes[0, 0].scatter(x_train, y_train, marker='x', c='r', label='Actual')
axes[0, 0].plot(x_train, preds, linestyle='-', color='blue', label='Predicted')
axes[0, 0].set_title("Data + Fitted Line")
axes[0, 0].set_xlabel("Area")
axes[0, 0].set_ylabel("Price")
axes[0, 0].legend()

# Plot 2: Cost over iterations
axes[0, 1].plot(costs, color='green')
axes[0, 1].set_title("Cost Function over Iterations")
axes[0, 1].set_xlabel("Iteration")
axes[0, 1].set_ylabel("Cost (MSE)")

# Plot 3: w over costs
axes[1, 0].plot(w_vals, costs, color='blue')
axes[1, 0].set_title("Parameter w over Costs")
axes[1, 0].set_xlabel("w")
axes[1, 0].set_ylabel("Cost")

# Plot 4: Tail plot
axes[1, 1].plot(100 + np.arange(len(costs[400:])), costs[400:], color='orange')
axes[1, 1].set_title("Costs over Iterations (tail)")
axes[1, 1].set_xlabel("Iteration")
axes[1, 1].set_ylabel("Cost (MSE)")

# Plot 5: Contour plot
w_range = np.linspace(100, 300, 100)
b_range = np.linspace(-100, 200, 100)
W, B = np.meshgrid(w_range, b_range)
Z = np.zeros_like(W)
for i in range(100):
    for j in range(100):
        Z[i, j] = cost_func(W[i, j], B[i, j])

cp = axes[0, 2].contour(W, B, Z, levels=30, cmap='RdYlGn_r')
axes[0, 2].clabel(cp, inline=True, fontsize=7)
axes[0, 2].plot(w_final, b_final, 'b*', markersize=12, label=f'min ({w_final:.1f}, {b_final:.1f})')
axes[0, 2].set_title("Contour Plot — Unscaled")
axes[0, 2].set_xlabel("w")
axes[0, 2].set_ylabel("b")
axes[0, 2].legend()

# Plot 6: b over iterations
axes[1, 2].plot(b_vals, color='purple')
axes[1, 2].set_title("Parameter b over Iterations")
axes[1, 2].set_xlabel("Iteration")
axes[1, 2].set_ylabel("b")

plt.tight_layout()
plt.show()

#  Final w: 209.36, Final b: 2.43
# Final cost: 1735.88