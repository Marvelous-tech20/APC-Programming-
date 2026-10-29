# 12. Pandas Series - student names and attendance percentages

import pandas as pd

attendance_dict = {"Amit": 60, "Priya": 90, "Rahul": 70, "Neha": 95, "Sam": 50}
attendance = pd.Series(attendance_dict)

print("Series:\n", attendance)

print("\nAverage attendance:", attendance.mean())

print("\nStudents with attendance below 75%:")
print(attendance[attendance < 75])

print("\nStudents with attendance above 90%:")
print(attendance[attendance > 90])

print("\nHighest attendance:", attendance.idxmax(), "-", attendance.max())
