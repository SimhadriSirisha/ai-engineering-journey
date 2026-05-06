import math
import numpy as np

# exercise : find the distance from center cell (1,1)

# with indices
rows, cols = np.indices((3, 3))
print("row: ", rows)
print("column: ", cols)

distance = np.sqrt((rows-1)**2 + (cols-1)**2) # this is where vectorization strategy will be used to skip the loop in numPy
print("distance: \n", distance)

# without indices
a = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        a[i][j] = math.sqrt((i-1)**2 + (j-1)**2)
print("a: \n", a)