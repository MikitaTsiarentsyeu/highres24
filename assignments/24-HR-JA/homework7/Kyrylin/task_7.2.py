def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) >= r:
        first, rest = lst[0], lst[1:]
        for combo in combinations(rest, r - 1):
            yield [first] + combo
        for combo in combinations(rest, r):
            yield combo

for combo in combinations([1, 2, 3, 4, 5, 6, 7], 3):
    print(combo)
