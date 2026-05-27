import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)

X, Y = np.meshgrid(x, y)

matrix = np.array([[1, 1],
                   [0, 1]])

points = np.array([X.flatten(), Y.flatten()])

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

transformations = [
    ("Shear", np.array([[1, 1], [0, 1]])),
    ("Rotation 90°", np.array([[0, -1], [1, 0]])),
    ("Scale x2", np.array([[2, 0], [0, 2]])),
    ("Collapse", np.array([[1, 1], [0, 0]])),
]


for idx, (name, matrix) in enumerate(transformations):
    transformed = matrix @ points

    x_new = transformed[0].reshape(X.shape)
    y_new = transformed[1].reshape(Y.shape)

    ax = axes[idx]

    for i in range(len(x)):
        ax.plot(X[:, i], Y[:, i], 'b-', linewidth=0.5)

    for i in range(len(y)):
        ax.plot(X[i, :], Y[i, :], 'b-', linewidth=0.5)

    for i in range(len(x)):
        ax.plot(x_new[:, i], y_new[:, i], 'r-', linewidth=0.5)

    for i in range(len(y)):
        ax.plot(x_new[i, :], y_new[i, :], 'r-', linewidth=0.5)

    # i-hat
    ax.annotate('', 
        xy=(1, 0),      # arrow tip
        xytext=(0, 0),           # arrow start (origin)
        arrowprops=dict(color='green', width=2)
    )
    # j-hat
    ax.annotate('', 
        xy=(0, 1),      # arrow tip
        xytext=(0, 0),           # arrow start (origin)
        arrowprops=dict(color='red', width=2)
    )

    transformed_i_hat = matrix[:,0]
    transformed_j_hat = matrix[:,1]

     # i-hat
    ax.annotate('', 
        xy=transformed_i_hat,      # arrow tip
        xytext=(0, 0),           # arrow start (origin)
        arrowprops=dict(color='green', width=2)
    )
    # j-hat
    ax.annotate('', 
        xy=transformed_j_hat,      # arrow tip
        xytext=(0, 0),           # arrow start (origin)
        arrowprops=dict(color='red', width=2)
    )

    ax.set_title(name)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)

plt.tight_layout()
plt.show()