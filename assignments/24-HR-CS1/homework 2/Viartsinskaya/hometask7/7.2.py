def combinations(lst, r):
    if r == 0:
        yield []
    else:
        for i in range(len(lst)):
            for combo in combinations(lst[i+1:], r-1):
                yield [lst[i]] + combo