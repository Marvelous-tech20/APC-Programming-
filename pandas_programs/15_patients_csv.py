# 15. Read patients.csv - above 60, avg expense, max expense, count per disease, expense>50000

import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical expense:", df["Medical_Expense"].mean())

top_patient = df.loc[df["Medical_Expense"].idxmax()]
print("\nPatient with highest medical expense:\n", top_patient)

print("\nCount of patients per disease:")
print(df["Disease"].value_counts())

print("\nPatients with medical expense > 50000:")
print(df[df["Medical_Expense"] > 50000])
