import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

subjects = ["Math", "Science", "English", "Computer"]

df["Total"] = df[subjects].sum(axis=1)

df["Percentage"] = (df["Total"] / 400) * 100

df["Average"] = df[subjects].mean(axis=1)

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(get_grade)

class_average = np.mean(df["Percentage"])

topper = df.loc[df["Total"].idxmax()]

print("\n===== STUDENT PERFORMANCE ANALYSIS =====\n")
print(df.to_string(index=False))

print("\n===== CLASS AVERAGE =====")
print("Average Percentage:", round(class_average, 2), "%")

print("\n===== TOPPER =====")
print("Name       :", topper["Name"])
print("Total Marks:", topper["Total"])
print("Percentage :", round(topper["Percentage"], 2), "%")
print("Grade      :", topper["Grade"])
