def combinations(lst, r):
    """Generate all r-length combinations from list"""
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(r, int) or r < 0 or r > len(lst):
        raise ValueError("r must be integer between 0 and list length")
    
    def helper(start, current):
        if len(current) == r:
            yield current.copy()
            return
        for i in range(start, len(lst)):
            current.append(lst[i])
            yield from helper(i+1, current)
            current.pop()
    
    yield from helper(0, [])

print(list(combinations(['a', 'b', 'c', 'd'], 2))) 