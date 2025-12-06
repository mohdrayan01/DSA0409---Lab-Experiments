from sklearn.linear_model import LogisticRegression
import numpy as np

# features: [usage_minutes, contract_months]
X = np.array([[100, 1],[200, 2],[300, 3],[400, 4],[500, 5]])
y = np.array([0,0,0,1,1])

logr = LogisticRegression()
logr.fit(X, y)

usage = float(input("Usage minutes: "))
months = float(input("Contract duration (months): "))

pred = logr.predict([[usage, months]])[0]
print("Churn prediction (0=no,1=yes):", pred)
