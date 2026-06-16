import numpy as np
import matplotlib.pyplot as plt
import gradientDescent as logisticReg

x_train = np.array([
    [0.5, 1.5], [1, 1], [1.5, 0.5], [1, 1.5], [0.5, 0.5],
    [3, 0.5], [2, 2], [2.5, 2.5], [3, 1], [2.5, 1.5],
    [0.3, 1.8], [1.8, 0.3]
])

y_train = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1])

pos = y_train == 1
neg = y_train == 0

iterations = 20000
W_final, b_final, costs = logisticReg.gradient_descent(iterations, 0.5, x_train, y_train, True, 10)
print(f"W_final : {W_final}")
print(f"b_final : {b_final}")

min = x_train[:, 0].min()
max = x_train[:, 0].max()
print(f"x1_train range: ({min, max})")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Gradient Descent — Logestic Regression", fontsize=14)

axes[0,0].plot(costs, color='green')
axes[0,0].set_title("Cost Function over Iterations")
axes[0,0].set_xlabel("Iteration")
axes[0,0].set_ylabel("Cost")

axes[0,1].plot(100 + np.arange(len(costs[400:])), costs[400:], color='orange')
axes[0,1].set_title("Costs over Iterations (tail)")
axes[0,1].set_xlabel("Iteration")
axes[0,1].set_ylabel("Cost")

axes[1,0].scatter(x_train[pos,0], x_train[pos,1], marker = 'x', c='red', label='y=1')
axes[1,0].scatter(x_train[neg,0], x_train[neg,1], marker = 'o', c='blue', label='y=0')
axes[1,0].set_title("train dataset")
axes[1,0].set_xlabel("x1")
axes[1,0].set_ylabel("x2")

# for decision boundry
x1_vals = np.linspace(min, max, 10)
x2_vals = -(W_final[0]*x1_vals + b_final) / W_final[1]
axes[1,1].scatter(x_train[pos,0], x_train[pos,1], marker = 'x', c='red', label='y=1')
axes[1,1].scatter(x_train[neg,0], x_train[neg,1], marker = 'o', c='blue', label='y=0')
axes[1,1].plot(x1_vals, x2_vals, 'k--')
axes[1,1].set_title("train dataset with decision boundry")
axes[1,1].set_xlabel("x1")
axes[1,1].set_ylabel("x2")

plt.tight_layout()
plt.show()

# here x1 is doing almost all the work(i.e. x1 dominates the decision) and x2 is not much important feature. That's why w1 is large and w2 is less i.e. -0.95
