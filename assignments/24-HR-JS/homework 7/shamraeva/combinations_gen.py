def combinations(lst, r):
    if r == 0:
        yield []
        return

    if len(lst) < r:
        return

    first, rest = lst[0], lst[1:]

    for combo in combinations(rest, r - 1):
        yield [first] + combo

    for combo in combinations(rest, r):
        yield combo