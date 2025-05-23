def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) >= r:
        firstElement = lst[0]
        modifiedList = lst[1:]
        for combo in combinations(modifiedList, r - 1):
            yield [firstElement] + combo
        for combo in combinations(modifiedList, r):
            yield combo


for combination in combinations([1, 4, 5, 6, 7], 3):
    print(combination)
