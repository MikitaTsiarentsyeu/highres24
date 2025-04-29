def combinations(lst, r):
    if r == 0:
        yield []
        return
    
    if r > len(lst):
        return
    
    for i in range(len(lst)):
        current = lst[i]
        for sub_combo in combinations(lst[i+1:], r-1):
            yield [current] + sub_combo


lst = [1, 2, 3, 4]
r = 2
for combo in combinations(lst, r):
    print(combo)  