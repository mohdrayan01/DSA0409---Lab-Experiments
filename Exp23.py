import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

control = np.array([120, 122, 121, 123, 119, 124])
treat = np.array([115, 117, 116, 114, 118, 113])

t_stat, p_val = stats.ttest_ind(control, treat, equal_var=False)
print("t-stat:", t_stat)
print("p-value:", p_val)

plt.boxplot([control, treat], labels=["Control", "Treatment"])
plt.title("BP Reduction: Control vs Treatment")
plt.ylabel("BP Level")
plt.show()
