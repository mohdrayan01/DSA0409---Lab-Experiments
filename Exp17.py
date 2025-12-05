import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")   # column: feedback
stop = {"the","and","is","a","an","to","of","in","on","for"}

all_txt = " ".join(df["feedback"].astype(str)).lower()
all_txt = all_txt.translate(str.maketrans("", "", string.punctuation))
words = [w for w in all_txt.split() if w not in stop]

freq = Counter(words)

n = int(input("Enter N: "))
top = freq.most_common(n)
print(top)

# bar plot
words_top = [w for w, c in top]
counts_top = [c for w, c in top]

plt.bar(words_top, counts_top)
plt.xlabel("Words")
plt.ylabel("Freq")
plt.title("Top N Words")
plt.show()
