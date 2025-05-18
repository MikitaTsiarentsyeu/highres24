def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        first = lst[0]
        rest = lst[1:]
        for combo in combinations(rest, r - 1):
            yield [first] + combo
        for combo in combinations(rest, r):
            yield combo
for c in combinations(['a', 'd', 'h'], 2):
    print(c)
