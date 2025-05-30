def fib_gen(n):
    first = 1
    second = 1
    if n >= 1:
        yield 1
    if n >= 2:
        yield 1
    for _ in range(n - 2):
        sum_fib = first + second
        yield sum_fib
        first = second
        second = sum_fib


for number in fib_gen(10):
    print(number)
