import numpy as np
marks = np.array([75,82,68,90,55,78,85,72,95,60,88,70,65,92,58,84,73])
average = np.mean(marks)
print("Class Average:", average)
print("Above Average:", marks[marks > average])