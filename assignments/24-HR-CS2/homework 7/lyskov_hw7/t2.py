def generate_combinations(lst, r):
    if r == 0:  
        yield []
    elif len(lst) < r:  
        return
    else:
        
        for combo in generate_combinations(lst[1:], r - 1):
            yield [lst[0]] + combo
        
     
        for combo in generate_combinations(lst[1:], r):
            yield combo


numbers = [1, 2, 3, 4, 5]
combination_length = 3

for combination in generate_combinations(numbers, combination_length):
    print(combination)