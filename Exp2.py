import numpy as np

sales_data = np.array([
    [200, 220, 210],
    [150, 160, 155],
    [300, 310, 305]
])

average_price = np.mean(sales_data)
print("Average Price of Products:", average_price)
