def combinations(lst, r):
    if r == 0:
        yield []
    elif r > len(lst): 
        return
    else:
        for i in range(len(lst)):
            for comb in combinations(lst[i + 1:], r - 1):
                yield [lst[i]] + comb

lst = [2,1,4,6]
r = 2

for comb in combinations(lst, r):
    print(comb)
