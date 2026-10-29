import numpy as np
arr = np.random.randint(1, 101, (2, 3, 4))
print("Original Array:")
print(arr)
arr[arr > 50] = 0
print("After replacement:")
print(arr)