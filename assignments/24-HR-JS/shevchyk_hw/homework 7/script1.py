def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) == 0:
        return
    else:
        first = lst[0]
        rest = lst[1:]

        for c in combinations(rest, r - 1):
            yield [first] + c

        for c in combinations(rest, r):
            yield c

for c in combinations(["a", "b", "c"], 2):
    print(c)
