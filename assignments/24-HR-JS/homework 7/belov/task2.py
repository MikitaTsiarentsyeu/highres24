def combinations(lst, r):
    if len(lst) < r:
        return
    if len(lst) == r:
        yield lst
    else:
        for i in range(len(lst)):
            yield from combinations([e for e in lst if e!=lst[i]], r)

listylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in combinations(listylist, 8):
    print(i)