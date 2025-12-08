import pandas as pd
from sklearn.cluster import KMeans

data = {
    "cust_id": [1,2,3,4,5],
    "freq": [5,10,3,20,15],
    "amount": [100,300,60,800,500]
}
df = pd.DataFrame(data)

X = df[["freq","amount"]]
km = KMeans(n_clusters=3, random_state=0)
df["cluster"] = km.fit_predict(X)

print(df)
