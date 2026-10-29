# 10. Pandas Series - product names and prices

import pandas as pd

price_dict = {"Pen": 10, "Notebook": 50, "Bag": 800, "Bottle": 150, "Watch": 1200}
prices = pd.Series(price_dict)

print("Original Series:\n", prices)

increased_prices = prices * 1.10
print("\nPrices after 10% increase:\n", increased_prices)

print("\nMost expensive product:", prices.idxmax(), "-", prices.max())

print("\nProducts costing more than 1000:")
print(prices[prices > 1000])
