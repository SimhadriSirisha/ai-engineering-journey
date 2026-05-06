import numpy as np

a = np.loadtxt("simple.csv", delimiter=",", skiprows=1)
print("a: ", a)