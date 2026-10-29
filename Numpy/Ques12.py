import numpy as np
arr = np.array([10, 60, 30, 75, 45, 90, 20, 55, 40, 80])
arr[arr > 50] = 0
print(arr)