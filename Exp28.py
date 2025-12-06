from sklearn.cluster import KMeans
import numpy as np

# features: [num_orders, total_spent]
X = np.array([[5, 100],[10, 300],[3, 50],[20, 800],[15, 500]])

km = KMeans(n_clusters=2, random_state=0)
km.fit(X)

orders = float(input("Orders: "))
spent = float(input("Total spent: "))

cluster = km.predict([[orders, spent]])[0]
print("Assigned cluster:", cluster)
