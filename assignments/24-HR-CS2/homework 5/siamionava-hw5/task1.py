def fibonacci(number: int) -> int:
    if number <= 0:
        print("n must be posistive")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    
n = input("write here a posistive number\n")
print(fibonacci(int(n)))