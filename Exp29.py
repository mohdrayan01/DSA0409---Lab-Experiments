from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
y = np.array([0,0,0,1,1,1])

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.33, random_state=0)

model = LogisticRegression()
model.fit(X_tr, y_tr)

y_pred = model.predict(X_te)

acc = accuracy_score(y_te, y_pred)
prec = precision_score(y_te, y_pred)
rec = recall_score(y_te, y_pred)
f1 = f1_score(y_te, y_pred)

print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1-score:", f1)
