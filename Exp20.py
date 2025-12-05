import numpy as np
from scipy import stats

A = np.array([0.05, 0.06, 0.055, 0.058, 0.06])
B = np.array([0.07, 0.072, 0.069, 0.071, 0.073])

t_stat, p_val = stats.ttest_ind(A, B, equal_var=False)

print("t-stat:", t_stat)
print("p-value:", p_val)
if p_val < 0.05:
    print("Statistically significant difference.")
else:
    print("No significant difference.")
