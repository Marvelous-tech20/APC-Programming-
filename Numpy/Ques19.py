import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print(arr)
print("First element:", arr[0, 0, 0])
print("Last element:", arr[-1, -1, -1])
print("Element [0,2,2]:", arr[0, 2, 2])
print("Element [1,2,3]:", arr[1, 2, 3])