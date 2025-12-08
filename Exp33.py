import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "engine": [1.2, 1.5, 2.0, 2.5],
    "hp": [80, 100, 150, 200],
    "fe": [18, 15, 12, 10],
    "price": [500000, 700000, 900000, 1200000]
}

df = pd.DataFrame(data)

X = df[["engine", "hp", "fe"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)


eng = float(input("Engine size (e.g. 1.5, 2.0): "))
hp = float(input("Horsepower (e.g. 100–150): "))
fe = float(input("Fuel efficiency (e.g. 10–18): "))

X_new = pd.DataFrame({
    "engine": [eng],
    "hp": [hp],
    "fe": [fe]
})

pred = model.predict(X_new)[0]

print("Predicted price:", pred)
print("R²:", model.score(X, y))
