from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target

clf = DecisionTreeClassifier()
clf.fit(X, y)

sl = float(input("Sepal length: "))
sw = float(input("Sepal width: "))
pl = float(input("Petal length: "))
pw = float(input("Petal width: "))

pred = clf.predict([[sl, sw, pl, pw]])[0]
print("Predicted species:", iris.target_names[pred])
