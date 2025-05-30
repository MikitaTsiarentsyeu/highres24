def fibonacci(n: int) -> int:
    first = 1
    second = 1
    i = 0
    sum_fib = 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        while i < n - 2:
            sum_fib = first + second
            first = second
            second = sum_fib
            i = i + 1
        return sum_fib


print(fibonacci(5))
print(fibonacci(6))
