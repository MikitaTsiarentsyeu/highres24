def Combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return lst
    else:

        for comb in Combinations(lst[1:], r - 1):
            yield [lst[0]] + comb

        for comb in Combinations(lst[1:], r):
            yield comb

items = ['a', 'b', 'c', 'd']
for comb in Combinations(items, 4):
    print(comb)