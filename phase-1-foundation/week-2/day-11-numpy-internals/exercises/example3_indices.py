import numpy as np

a = np.indices((2, 3))
print("Indices of the array: ", a)
print("a shape: ", a.shape)

# indices returns an grid of indices of the array 2X3
# [[0,0], [0,1], [0, 2]]
# [[1,0], [1,1], [1, 2]]

# These indices are seperated for each grid
# grid 0 (what is the row no of each grid cell)
# [[0,0]->0, [0,1]->0, [0, 2]->0]
# [[1,0]->1, [1,1]->1, [1, 2]->1]
# final grid 0 :
# [[0,0,0],
#  [1,1,1]]


# grid 1 (what is the column no of each grid cell)
# [[0,0]->0, [0,1]->1, [0, 2]->2]
# [[1,0]->0, [1,1]->1, [1, 2]->2]
# final grid 1 :
# [[0,1,2],
#  [0,1,2]]

# final ndarray :
# [[[0,0,0],
#   [1,1,1]],
#  [[0,1,2],
#   [0,1,2]]]