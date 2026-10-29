# 5. Order dictionary -> DataFrame - final amount, orders>5000, highest/avg order value

import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4],
    "Customer": ["Amit", "Priya", "Ravi", "Neha"],
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "Quantity": [1, 2, 1, 3],
    "Price": [50000, 15000, 20000, 1000],
    "Discount": [2000, 1000, 500, 100]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:\n", df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

highest_order = df.loc[df["Final_Amount"].idxmax()]
print("\nHighest-value order:\n", highest_order)

print("\nAverage order value:", df["Final_Amount"].mean())
