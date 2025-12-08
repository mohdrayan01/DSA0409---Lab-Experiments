import pandas as pd

df = pd.read_csv("stock_data.csv")  # column: close

mean = df["close"].mean()
std = df["close"].std()
min_p = df["close"].min()
max_p = df["close"].max()

print("Mean close:", mean)
print("Std dev:", std)
print("Min:", min_p, "Max:", max_p)
