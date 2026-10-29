# 11. Pandas Series - patient IDs (index) and ages

import pandas as pd

age_dict = {"P1": 65, "P2": 45, "P3": 70, "P4": 55, "P5": 80}
ages = pd.Series(age_dict)

print("Series:\n", ages)

print("\nAverage age:", ages.mean())
print("Oldest patient:", ages.idxmax(), "-", ages.max())
print("Youngest patient:", ages.idxmin(), "-", ages.min())

print("\nPatients above 60 years:")
print(ages[ages > 60])
