def combinations(lst, r):
    if r == 0: # Return nothing, because zero
        yield []
    elif len(lst) < r: # Error, because not enough elements
        return
    else:
        for combo in combinations(lst[1:], r - 1):  # Include the first element
            yield [lst[0]] + combo
        for combo in combinations(lst[1:], r): # Exclude the first element
            yield combo

for c in combinations([1, 2, 3, 4, 5], 3):
    print(c)
