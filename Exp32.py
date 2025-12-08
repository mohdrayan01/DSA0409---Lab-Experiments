import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "size": [1000, 1500, 2000, 2500, 3000],
    "price": [200000, 250000, 300000, 350000, 400000]
}
df = pd.DataFrame(data)

X = df[["size"]]   # feature with name 'size'
y = df["price"]    # target

model = LinearRegression()
model.fit(X, y)

s = float(input("Enter house size (in sq.ft): "))

X_new = pd.DataFrame({"size": [s]})
pred = model.predict(X_new)[0]

print("Predicted price:", pred)
print("R^2:", model.score(X, y))
