def combinations(lst, r):
    if r == 0:
        yield []
        return

    if len(lst) < r:
        return
    
    for list in combinations(lst[1:], r - 1):
        yield [lst[0]] + list

    for list in combinations(lst[1:], r):
        yield list

lst = [1, 2, 3, 4]
r = 1
for list in combinations(lst, r):
    print(list)