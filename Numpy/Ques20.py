import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Total sum:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows:", np.sum(arr, axis=2))
print("Sum along columns:", np.sum(arr, axis=1))