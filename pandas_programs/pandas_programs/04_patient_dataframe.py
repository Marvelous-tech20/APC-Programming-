# 4. Patient dictionary -> DataFrame - above 60, avg charge, max charge, charges>50000

import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Ramesh", "Sita", "Mohan", "Geeta", "Vijay"],
    "Age": [65, 45, 70, 55, 80],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Cold", "Arthritis"],
    "Medical_Charges": [60000, 5000, 90000, 2000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())

print("\nPatients with medical charges > 50000:")
print(df[df["Medical_Charges"] > 50000])
