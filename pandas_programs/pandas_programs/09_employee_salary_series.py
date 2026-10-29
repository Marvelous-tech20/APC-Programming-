# 9. Pandas Series - employee names and salaries

import pandas as pd

salary_dict = {"Ravi": 45000, "Meena": 60000, "John": 55000, "Asha": 70000, "Kiran": 40000}
salaries = pd.Series(salary_dict)

print("Series:\n", salaries)

print("\nHighest salary:", salaries.max())
print("Lowest salary:", salaries.min())
print("Average salary:", salaries.mean())

print("\nEmployees earning more than 50000:")
print(salaries[salaries > 50000])
