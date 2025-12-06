import pandas as pd
from scipy import stats
import numpy as np

df = pd.read_csv("customer_reviews.csv")  # column: rating
r = df["rating"].dropna()

conf = 0.95
mean = r.mean()
se = stats.sem(r)
t = stats.t.ppf((1+conf)/2, len(r)-1)
low = mean - t*se
high = mean + t*se

print("Mean rating:", mean)
print("95% CI:", (low, high))
