# 3. Product dictionary -> DataFrame - total amount, highest total sales product

import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4],
    "Product_Name": ["Pen", "Notebook", "Bag", "Bottle"],
    "Category": ["Stationery", "Stationery", "Accessories", "Accessories"],
    "Price": [10, 50, 800, 150],
    "Quantity": [100, 60, 20, 40]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("DataFrame:\n", df)

top_product = df.loc[df["Total_Amount"].idxmax()]
print("\nProduct with highest total sales:\n", top_product)
