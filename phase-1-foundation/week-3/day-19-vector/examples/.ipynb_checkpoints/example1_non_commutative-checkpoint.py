import numpy as np
A = np.array([[1,1],[0,1]])  # shear
B = np.array([[0,-1],[1,0]]) # rotation 90°

print(A @ B)  # shear then rotate
print(B @ A)  # rotate then shear