import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = {
    "age":  [30, 35, 40, 45, 50, 55, 60, 65],
    "bp":   [120,125,130,135,140,145,150,155],
    "chol": [200,210,220,230,240,250,260,270],
    "outcome": ["Good","Good","Good","Bad","Bad","Bad","Bad","Good"]
}

df = pd.DataFrame(data)

X = df[["age","bp","chol"]]
y = (df["outcome"] == "Good").astype(int)

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

knn = KNeighborsClassifier(n_neighbors=1)  # ✅ smaller k works better here
knn.fit(X_tr, y_tr)

y_pred = knn.predict(X_te)

print("Actual:", y_te.values)
print("Predicted:", y_pred)

print("Accuracy:", accuracy_score(y_te, y_pred))
print("Precision:", precision_score(y_te, y_pred, zero_division=0))
print("Recall:", recall_score(y_te, y_pred, zero_division=0))
print("F1:", f1_score(y_te, y_pred, zero_division=0))
