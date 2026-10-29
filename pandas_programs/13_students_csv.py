# 13. Read students.csv - first5, last5, total/avg, >75, topper, subject-wise avg

import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and average marks of each student:\n", df[["Name", "Total", "Average"]])

print("\nStudents with average marks > 75:")
print(df[df["Average"] > 75])

topper = df.loc[df["Average"].idxmax()]
print("\nStudent with highest average:\n", topper)

print("\nAverage marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())
