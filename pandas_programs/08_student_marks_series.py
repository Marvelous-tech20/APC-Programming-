# 8. Pandas Series - student names (keys) and marks (values)

import pandas as pd

marks_dict = {"Amit": 85, "Priya": 92, "Rahul": 60, "Neha": 78, "Sam": 95}
marks = pd.Series(marks_dict)

print("Series:\n", marks)

print("\nMarks of Priya:", marks["Priya"])
print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Average marks:", marks.mean())

print("\nStudents who scored more than 75:")
print(marks[marks > 75])
