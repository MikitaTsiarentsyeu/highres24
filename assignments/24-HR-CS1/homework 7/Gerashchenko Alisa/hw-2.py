def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        for tail in combinations(lst[1:], r - 1):
            yield [lst[0]] + tail
        for tail in combinations(lst[1:], r):
            yield tail

for comb in combinations(['a', 'b', 'c', 'd', 'f'], 2):
    print(comb)