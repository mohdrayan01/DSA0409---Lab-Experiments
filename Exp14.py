import pandas as pd
from collections import Counter

ages = [22, 25, 22, 30, 25, 22, 35]
df = pd.DataFrame({"age": ages})

freq = Counter(df["age"])
for a, c in freq.items():
    print(a, ":", c)
