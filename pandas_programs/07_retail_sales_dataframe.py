# 7. Retail shop dictionary -> DataFrame - Total_Sales column, filter, max, avg

import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["TV", "Fridge", "Mixer", "Fan", "AC"],
    "Category": ["Electronics", "Electronics", "Appliance", "Appliance", "Electronics"],
    "Price": [30000, 25000, 2000, 1500, 40000],
    "Quantity": [5, 4, 10, 15, 3]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:\n", df)

print("\nProducts with sales > 10000:")
print(df[df["Total_Sales"] > 10000])

top_product = df.loc[df["Total_Sales"].idxmax()]
print("\nProduct with maximum sales:\n", top_product)

print("\nAverage sales:", df["Total_Sales"].mean())
