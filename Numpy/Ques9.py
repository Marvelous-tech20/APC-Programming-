import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal:", np.diag(arr))
print("Second and third rows:")
print(arr[1:3])