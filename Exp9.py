import pandas as pd

data = {
    "prop_id": [1, 2, 3, 4],
    "loc": ["CityA", "CityA", "CityB", "CityB"],
    "beds": [3, 5, 4, 6],
    "area": [1200, 2000, 1500, 2500],
    "price": [300000, 500000, 350000, 600000]
}
df = pd.DataFrame(data)

avg_price_loc = df.groupby("loc")["price"].mean()
more4 = df[df["beds"] > 4].shape[0]
largest = df.loc[df["area"].idxmax()]

print("Avg price per location:\n", avg_price_loc)
print("\nProperties with >4 beds:", more4)
print("\nProperty with largest area:\n", largest)
