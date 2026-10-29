# 16. Read weather.csv - max/min/avg temp, temp>35, city-wise avg temp

import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum temperature:", df["Temperature"].max())
print("Minimum temperature:", df["Temperature"].min())
print("Average temperature:", df["Temperature"].mean())

print("\nRecords with temperature above 35:")
print(df[df["Temperature"] > 35])

print("\nCity-wise average temperature:")
print(df.groupby("City")["Temperature"].mean())
