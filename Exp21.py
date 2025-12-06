import numpy as np
from scipy import stats

# Load data (skip header row)
data = np.loadtxt("rare_elements.csv", skiprows=1)

n = int(input("Enter sample size: "))
conf = float(input("Enter confidence level (e.g. 0.95): "))

sample = np.random.choice(data, size=n, replace=False)

mean = np.mean(sample)
se = stats.sem(sample)
t = stats.t.ppf((1 + conf) / 2, n - 1)

low = mean - t * se
high = mean + t * se

print("Sample mean:", mean)
print(f"{int(conf*100)}% Confidence Interval: ({low}, {high})")
