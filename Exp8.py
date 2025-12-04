import pandas as pd

data = {
    "prod": ["A", "B", "A", "C", "B", "A", "D"],
    "qty":  [5,   2,   3,   4,   6,   1,   7]
}
df = pd.DataFrame(data)

top = df.groupby("prod")["qty"].sum().sort_values(ascending=False).head(5)
print(top)
