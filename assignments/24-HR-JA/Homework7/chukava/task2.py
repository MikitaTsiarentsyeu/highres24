def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        for combo in combinations(lst[1:], r - 1):
            yield [lst[0]] + combo
        for combo in combinations(lst[1:], r):
            yield combo

items = ['a', 'b', 'c', 'd']
for combo in combinations(items, 2):
    print(combo)