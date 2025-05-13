def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        # Include lst[0]
        for rest in combinations(lst[1:], r - 1):
            yield [lst[0]] + rest
        # Exclude lst[0]
        for rest in combinations(lst[1:], r):
            yield rest
