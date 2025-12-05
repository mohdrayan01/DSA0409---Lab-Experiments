import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
temp = [25, 26, 28, 30]
rain = [80, 60, 40, 20]

# Line plot for temperature
plt.plot(months, temp, marker="o")
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temp (°C)")
plt.show()

# Scatter plot for rainfall
plt.scatter(months, rain)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
