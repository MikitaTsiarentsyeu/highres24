def combinations(lst, r):
    if r == 0:
        yield []
        return
    if len(lst) < r:
        return
    
    for sub_comb in combinations(lst[1:], r - 1):
        yield [lst[0]] + sub_comb

    for sub_comb in combinations(lst[1:], r):
        yield sub_comb
