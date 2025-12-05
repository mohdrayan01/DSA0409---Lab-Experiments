from collections import Counter

with open("sample_text.txt", "r") as f:
    txt = f.read()

words = txt.lower().split()
freq = Counter(words)

for w, c in freq.items():
    print(w, ":", c)
