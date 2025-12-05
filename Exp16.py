from collections import Counter

reviews = [
    "Good product and fast delivery",
    "Very good quality",
    "Delivery was slow but product is good"
]

txt = " ".join(reviews).lower().split()
freq = Counter(txt)

for w, c in freq.items():
    print(w, ":", c)
