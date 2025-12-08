import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "cust_id":[1,2,3,4,5],
    "amount":[100,300,50,800,500],
    "items":[2,5,1,10,7]
}
df = pd.DataFrame(data)

X = df[["amount","items"]]
km = KMeans(n_clusters=3, random_state=0)
df["cluster"] = km.fit_predict(X)

print(df)

plt.scatter(df["amount"], df["items"], c=df["cluster"])
plt.xlabel("Amount spent")
plt.ylabel("Items purchased")
plt.title("Customer Segments")
plt.show()
