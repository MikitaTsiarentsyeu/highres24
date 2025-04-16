def combinations(lst, r):
    if r == 0:
        yield []
        return
    if len(lst) < r:
        return

    
    for i in range(len(lst)):
      
        for combo in combinations(lst[i+1:], r-1):
            yield [lst[i]] + combo

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4]
    r = 2
    print(f"All combinations of size {r} from {sample_list}:")
    for combo in combinations(sample_list, r):
        print(combo)
