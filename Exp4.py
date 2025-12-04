import numpy as np

sales_data = np.array([200000, 250000, 300000, 350000])

total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Annual Sales:", total_sales)
print("Percentage Increase from Q1 to Q4:", percentage_increase, "%")
