def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) >= r:
        firstElement = lst[0]
        modifiedList = lst[1:]
        for i in combinations(modifiedList, r - 1):
            yield [firstElement] + i
        for i in combinations(modifiedList, r):
            yield i
    else:
        return

for combination in combinations([1, 2, 3, 4, 5, 6, 7], 3):
    print(combination)




