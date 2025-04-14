text = input().lower().split()
d = {}
for w in text:
    d[w] = d.get(w, 0) + 1
items = [(c, w) for w, c in d.items()]
for c, w in sorted(items):
    print(w, c)
