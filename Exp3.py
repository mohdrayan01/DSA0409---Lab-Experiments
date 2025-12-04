import numpy as np

house_data = np.array([
    [3, 1200, 250000],
    [5, 2000, 400000],
    [4, 1500, 300000],
    [6, 2500, 500000]
])

filtered_prices = house_data[house_data[:, 0] > 4, 2]
average_price = np.mean(filtered_prices)

print("Average Price of Houses with > 4 Bedrooms:", average_price)
