def combinations(lst, r):
    if r == 0:
        yield []
    elif r > len(lst): 
        return
    else:
        for i in range(len(lst)):
            for comb in combinations(lst[i + 1:], r - 1):
                yield [lst[i]] + comb

lst = ["f","s","r","k","l"]
r = 3

for comb in combinations(lst, r):
    print(comb)