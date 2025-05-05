def combinations(lst, r):
    if r == 0:
        yield []
    elif len(lst) < r:
        return
    else:
        first = lst[0]
        for combo in combinations(lst[1:], r-1):
            yield [first] + combo
        
        yield from combinations(lst[1:], r)
        

print(list(combinations([1, 2, 3, 4, 5], 3)))