def combinations(lst, r):
    if r == 0:
        yield []
        return
    if not lst or r > len(lst):
        return

    first = lst[0]
    rest = lst[1:]

    for combo in combinations(rest, r - 1):
        yield [first] + combo

    for combo in combinations(rest, r):
        yield combo

print(list(combinations([1, 2, 3, 4, 5], 2)))