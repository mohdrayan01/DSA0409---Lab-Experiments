import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 130, 180]

# Line plot
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Line")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar plot
plt.bar(months, sales)
plt.title("Monthly Sales - Bar")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
