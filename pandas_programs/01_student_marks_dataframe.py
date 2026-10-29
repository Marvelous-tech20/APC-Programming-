import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Student_Name": ["Amit", "Priya", "Rahul", "Neha", "Sam"],
    "Python_Marks": [85, 90, 60, 75, 95],
    "DBMS_Marks": [78, 88, 65, 70, 92],
    "Maths_Marks": [92, 85, 70, 80, 89]
}

df = pd.DataFrame(data)

df["Total_Marks"] = df["Python_Marks"] + df["DBMS_Marks"] + df["Maths_Marks"]
df["Average_Marks"] = df["Total_Marks"] / 3

print("DataFrame:\n", df)

print("\nStudents with average > 75%:")
print(df[df["Average_Marks"] > 75])
