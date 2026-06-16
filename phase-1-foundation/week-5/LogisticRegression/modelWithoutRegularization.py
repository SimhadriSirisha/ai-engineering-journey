from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt
import gradientDescent as logisticReg

x_train = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])  #(m,n) -> (6,2)
y_train = np.array([0, 0, 0, 1, 1, 1])                                           #(m,) -> (6,)

pos = y_train == 1 # [false, false, false, true, true, true]
neg = y_train == 0 # [true, true, true, false, false, false]

# plt.scatter(x_train[pos,0], x_train[pos,1], marker = 'x', c='red', label='y=1')
# plt.scatter(x_train[neg,0], x_train[neg,1], marker = 'o', c='blue', label='y=0')

# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.legend()
# plt.show()

iterations = 20000
W_final, b_final, costs = logisticReg.gradient_descent(iterations, 0.5, x_train, y_train, False)
print(f"W_final : {W_final}")
print(f"b_final : {b_final}")

min = x_train[:, 0].min()
max = x_train[:, 0].max()
print(f"x1_train range: ({min, max})")

fig, axes = plt.subplots(1, 3, figsize=(18, 7))
fig.suptitle("Gradient Descent — Logestic Regression", fontsize=14)

axes[0].plot(costs, color='green')
axes[0].set_title("Cost Function over Iterations")
axes[0].set_xlabel("Iteration")
axes[0].set_ylabel("Cost")

axes[1].plot(100 + np.arange(len(costs[400:])), costs[400:], color='orange')
axes[1].set_title("Costs over Iterations (tail)")
axes[1].set_xlabel("Iteration")
axes[1].set_ylabel("Cost")

# for decision boundry
x1_vals = np.linspace(min, max, 100)
x2_vals = -(W_final[0]*x1_vals + b_final) / W_final[1]
axes[2].scatter(x_train[pos,0], x_train[pos,1], marker = 'x', c='red', label='y=1')
axes[2].scatter(x_train[neg,0], x_train[neg,1], marker = 'o', c='blue', label='y=0')
axes[2].plot(x1_vals, x2_vals, 'k--')
axes[2].set_title("train dataset with decision boundry")
axes[2].set_xlabel("x1")
axes[2].set_ylabel("x2")

plt.tight_layout()
plt.show()