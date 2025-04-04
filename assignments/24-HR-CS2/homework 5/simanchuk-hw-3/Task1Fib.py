# Task 1 - Fibonacci Sequence
# Write a function which will return rhe n-th number of the Fibonacci Sequence

def fibonacci(n:int)-> int:
    if n <= 0:
        print("n should be > 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(21))