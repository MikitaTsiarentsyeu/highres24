def combinations(lst, r):
    def comb_recursive(start, chosen):
        if len(chosen) == r:
            yield chosen
            return
        for i in range(start, len(lst)):
            yield from comb_recursive(i + 1, chosen + [lst[i]])

    yield from comb_recursive(0, [])

# Example
lst = [1, 2, 3, 4]
r = 2
for comb in combinations(lst, r):
    print(comb)