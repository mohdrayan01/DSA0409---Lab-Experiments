from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# features: [symptom1, symptom2]
X = np.array([[1,2],[2,3],[3,3],[4,5],[5,5]])
y = np.array([0,0,1,1,1])

k = int(input("Enter k: "))
s1 = float(input("Enter symptom1: "))
s2 = float(input("Enter symptom2: "))

knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

pred = knn.predict([[s1, s2]])[0]
print("Prediction (0=no, 1=yes):", pred)
