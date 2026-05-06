import numpy as np
import time

# without NumPy
a = list(range(1, 10000001))
loop_time = 0
start = time.perf_counter()
for item in a:
    loop_time += item
end = time.perf_counter()
print(f"Total summation time took without NumPy library: {end - start}")

# with NumPy
b = np.arange(1, 10000001, dtype=np.int64)
start = time.perf_counter()
numpy_time = np.sum(b)
end = time.perf_counter()
print(f"Total summation time took with NumPy library: {end - start}")

print(f"Is summation equal: {loop_time == numpy_time}")

speedup = loop_time / numpy_time
print(f"Speedup: {speedup}")