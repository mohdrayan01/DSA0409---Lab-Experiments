import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [10, 15, 13, 20, 18]

# 1. Line plot
plt.plot(days, sales, marker="o")
plt.title("Sales per Day - Line")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

# 2. Scatter plot
plt.scatter(days, sales)
plt.title("Sales per Day - Scatter")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

# 3. Bar plot
plt.bar(days, sales)
plt.title("Sales per Day - Bar")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()
