import pandas as pd

data = {
    "cust_id": [1, 1, 2, 3, 2],
    "date": ["2024-01-01", "2024-01-05", "2024-01-03", "2024-01-04", "2024-01-06"],
    "prod": ["A", "B", "A", "C", "B"],
    "qty": [2, 1, 3, 5, 2]
}
df = pd.DataFrame(data)

orders_per_cust = df.groupby("cust_id")["prod"].count()
avg_qty_per_prod = df.groupby("prod")["qty"].mean()
min_date = df["date"].min()
max_date = df["date"].max()

print("Orders per customer:\n", orders_per_cust)
print("\nAvg qty per product:\n", avg_qty_per_prod)
print("\nEarliest date:", min_date)
print("Latest date:", max_date)
