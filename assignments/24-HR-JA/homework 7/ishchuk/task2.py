def combinations(lst, r):
    if r == 0:
        yield []
        return
    if len(lst) == 0:
        return

    first = lst[0]
    rest = lst[1:]

    for combo in combinations(rest, r - 1):
        yield [first] + combo

    for combo in combinations(rest, r):
        yield combo

items = ['a', 'b', 'c']
for c in combinations(items, 2):
    print(c)
