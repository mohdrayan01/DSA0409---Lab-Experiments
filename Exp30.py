from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text
import numpy as np

# features: [mileage, age]
X = np.array([[50000,5],[30000,3],[70000,7],[20000,2]])
y = np.array([300000, 350000, 250000, 400000])

tree = DecisionTreeRegressor(random_state=0)
tree.fit(X, y)

mil = float(input("Mileage: "))
age = float(input("Age (years): "))

pred = tree.predict([[mil, age]])[0]
print("Predicted price:", pred)

r = export_text(tree, feature_names=["mileage","age"])
print("\nDecision tree:\n", r)
