def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        for combination in combinations(lst[1:], r - 1):
            yield [lst[0]] + combination  # combo with 0 element
        for combination in combinations(lst[1:], r):
            yield combination


combinations_list = [1, 2, 3, 4]
for comb in combinations(combinations_list, 2):
    print(comb)
