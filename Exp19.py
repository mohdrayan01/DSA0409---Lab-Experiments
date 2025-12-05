import numpy as np
from scipy import stats

drug = np.array([8, 10, 12, 9, 11, 13, 7, 10])
placebo = np.array([2, 3, 1, 4, 2, 3, 1, 2])

conf = 0.95

def ci_95(x):
    n = len(x)
    mean = np.mean(x)
    se = stats.sem(x)
    t = stats.t.ppf((1+conf)/2, n-1)
    low = mean - t*se
    high = mean + t*se
    return mean, low, high

m1, l1, h1 = ci_95(drug)
m2, l2, h2 = ci_95(placebo)

print("Drug mean:", m1, "CI:", (l1, h1))
print("Placebo mean:", m2, "CI:", (l2, h2))
