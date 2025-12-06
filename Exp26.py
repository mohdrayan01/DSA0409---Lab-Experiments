from sklearn.linear_model import LinearRegression
import numpy as np

# features: [area, bedrooms]
X = np.array([[1000,2],[1500,3],[2000,3],[2500,4]])
y = np.array([200000, 250000, 300000, 380000])

lr = LinearRegression()
lr.fit(X, y)

area = float(input("Enter area: "))
beds = int(input("Enter bedrooms: "))

pred = lr.predict([[area, beds]])[0]
print("Predicted price:", pred)
