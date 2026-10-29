# 6. Student attendance dictionary -> DataFrame - attendance %, below 75%

import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Sam"],
    "Department": ["CSE", "CSE", "IT", "IT", "CSE"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [60, 90, 70, 95, 50]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("DataFrame:\n", df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])
