import numpy as np

a = np.array([1, 2, 3, 4])
print("a: ", a)

b = a[:2]
print("b: ", b)

b += 1
print("b: ", b)
print("a: ", a) # 'a' changed because here we just created a view or reference to 'a' named as 'b', so any change to 'b' will reflect 'a'

# so for update seperatly
c = a[:2].copy()
c += 1
print("c: ", c)
print("a: ", a)