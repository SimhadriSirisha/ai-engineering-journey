import numpy as np
a = np.arange(15).reshape(3, 5)
print("ndarray a: \n", a)
print("ndarray a shape: ", a.shape)
print("ndarray a ndim: ", a.ndim)
print("ndarray a dtype: ", a.dtype)
print("ndarray a dtype name: ", a.dtype.name)
print("ndarray a itemsize: ", a.itemsize)
print("ndarray a size: ", a.size)
print("ndarray a nbytes: ", a.nbytes)
print("ndarray a type: ", type(a))

# b = np.arange(15).reshape(2, 5) -> it is an error because 15 elements cannot be reshaped into 2 rows and 5 columns and will get ValueError
# print("ndarray b: \n", b)