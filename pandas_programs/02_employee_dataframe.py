# 2. Employee dictionary -> DataFrame - salary filter, avg, highest, most experienced

import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Ravi", "Meena", "John", "Asha", "Kiran"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales"],
    "Salary": [45000, 60000, 55000, 70000, 40000],
    "Experience": [2, 5, 3, 7, 1]
}

df = pd.DataFrame(data)

print("Employees with salary > 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())

most_experienced = df.loc[df["Experience"].idxmax()]
print("\nEmployee with highest experience:\n", most_experienced)
