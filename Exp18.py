import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

age = [23, 25, 30, 35, 40, 45]
fat = [18.5, 20.1, 22.0, 24.5, 26.0, 27.3]

df = pd.DataFrame({"age": age, "%fat": fat})

print("Age mean:", df["age"].mean())
print("Age median:", df["age"].median())
print("Age std:", df["age"].std())

print("Fat mean:", df["%fat"].mean())
print("Fat median:", df["%fat"].median())
print("Fat std:", df["%fat"].std())

df[["age","%fat"]].boxplot()
plt.title("Boxplot of Age and %Fat")
plt.show()

plt.scatter(df["age"], df["%fat"])
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.title("Scatter Age vs %Fat")
plt.show()

stats.probplot(df["%fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of %Fat")
plt.show()
