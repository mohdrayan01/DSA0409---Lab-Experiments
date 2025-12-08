import pandas as pd
import matplotlib.pyplot as plt

# assume CSV already created
# columns: name, age, pos, goals, salary
df = pd.read_csv("players.csv")

top_goals = df.sort_values("goals", ascending=False).head(5)
top_salary = df.sort_values("salary", ascending=False).head(5)

print("Top 5 by goals:\n", top_goals[["name","goals"]])
print("\nTop 5 by salary:\n", top_salary[["name","salary"]])

avg_age = df["age"].mean()
print("\nAverage age:", avg_age)

above = df[df["age"] > avg_age]["name"]
print("Players above avg age:\n", above.values)

pos_counts = df["pos"].value_counts()
plt.bar(pos_counts.index, pos_counts.values)
plt.xlabel("Position")
plt.ylabel("Count")
plt.title("Players per Position")
plt.show()
