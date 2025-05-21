def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        for combinat in combinations(lst[1:], r - 1):
            yield [lst[0]] + combinat
        for combinat in combinations(lst[1:], r):
            yield combinat

comb_list = [1, 2, 3, 4]
for comb in combinations(comb_list, 2):
    print(comb)
