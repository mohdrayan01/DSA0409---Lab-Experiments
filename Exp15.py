from collections import Counter

likes = [10, 5, 10, 20, 5, 5, 15]

freq = Counter(likes)
for l, c in freq.items():
    print(l, "likes :", c, "posts")
