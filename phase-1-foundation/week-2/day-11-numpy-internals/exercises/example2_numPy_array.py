import numpy as np

# 1. Converting Python sequences to NumPy arrays
a1D = np.array([1, 2, 3])
print("1D array: ", a1D)

a2D = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array: ", a2D)

a3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D array: ", a3D)

aWithDType = np.array([1, 2, 3], dtype=np.float32)
print("Array with dtype: ", aWithDType)

# 2. Intrinsic NumPy array creation functions (Note: best practice for numpy.arange is to use integer start, end, and step values.)
b1 = np.arange(10)
print("Array from arange: ", b1)

b2 = np.arange(10, 20, dtype=np.float32)
print("Array from arange with dtype: ", b2)

b3 = np.arange(10, 20, 1.0)
print("Array from arange with step: ", b3)

b4 = np.linspace(0, 1, 5)
print("Array from linspace: ", b4) # returns 5 evenly spaced samples in the interval [0,1] & end is inclusive

b2D = np.eye(3) # returns 2D identity matrix of size 3x3
print("2D identity matrix: ", b2D)

b2DWithDifferentSize = np.eye(3, 4) # returns 2D identity matrix of size 3x4, and 1 will be filled where row index i == column index j
print("2D identity matrix with different size: ", b2DWithDifferentSize)

b2DSquareMatrix = np.diag([1, 2, 3]) # returns 2D square matrix of size 3x3, and 1, 2, 3 will be filled in the diagonal
print("2D square matrix: ", b2DSquareMatrix)

diagnalElements = np.diagonal(b2DSquareMatrix) # returns the diagonal elements of the matrix
print("Diagonal elements: ", diagnalElements)

b2DVendermondeMatrix = np.vander([1, 2, 3, 4]) # returns the Vandermonde matrix of the given array (a matrix with elements as powers of the given elements, highest power = n-1)
print("Vandermonde matrix: ", b2DVendermondeMatrix)
# here power = 4 - 1 = 3 
# o/p = [[1^3 1^2 1^1 1^0]
#        [2^3 2^2 2^1 2^0]
#        [3^3 3^2 3^1 3^0]
#        [4^3 4^2 4^1 4^0]]    

#     = [[1 1 1 1]
#        [8 4 2 1]
#        [27 9 3 1]
#        [64 16 4 1]]    

b2DWithLinespace = np.vander(np.linspace(0, 1, 5), 3)
print("Vandermonde matrix with linspace: ", b2DWithLinespace)

matrixWithAllZeros = np.zeros((2, 3))
print("Array with all zeros: ", matrixWithAllZeros)

matrixWithAllOnes = np.ones((2, 3))
print("Array with all ones: ", matrixWithAllOnes)

from numpy.random import default_rng
rng = default_rng(42) # 42 is the seed for random number generator
randomArray = rng.random((2, 3)) # returns a 2D array of size 2x3 with random floats between 0 and 1
print("Random array: ", randomArray)

randomArrayWithDifferentSize = rng.random((2, 3, 4)) # returns a 3D array of size 2x3x4 with random floats between 0 and 1
print("Random array with different size: ", randomArrayWithDifferentSize)