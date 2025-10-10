def combinations(lst, r):
    if r == 0:
        yield []
        return
        
    if len(lst) < r:
        return
        
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[i + 1:]
        
        for combo in combinations(remaining, r - 1):
            yield [current] + combo

if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    r = 2
    print(f"All combinations of size {r} from {test_list}:")
    for combo in combinations(test_list, r):
        print(combo)
