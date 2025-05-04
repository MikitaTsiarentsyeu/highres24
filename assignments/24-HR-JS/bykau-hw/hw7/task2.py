def combinations(lst, r):
    if r == 0:
        yield []
        return
    if not lst:
        return
    for rest in combinations(lst[1:], r-1):
        yield [lst[0]] + rest
    for rest in combinations(lst[1:], r):
        yield rest


for c in combinations([1, 2, 3, 4], 3):
    print(c)
