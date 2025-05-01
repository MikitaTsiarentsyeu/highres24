def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) == 0:
        return

    else:
        first = lst[0]
        rest = lst[1:]
        for combo in combinations(rest, r - 1):
            yield [first] + combo
        for combo in combinations(rest, r):
            yield combo

for c in combinations([1, 2, 3, 4, 5], 2):
    print(c)
