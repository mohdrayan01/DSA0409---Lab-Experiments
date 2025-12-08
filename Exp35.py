import pandas as pd
from sklearn.cluster import KMeans

data = {
    "cust_id":[1,2,3,4,5],
    "amount":[100,300,50,800,500],
    "visits":[2,5,1,10,7]
}
df = pd.DataFrame(data)

X = df[["amount","visits"]]
km = KMeans(n_clusters=2, random_state=0)
df["cluster"] = km.fit_predict(X)

print(df)
