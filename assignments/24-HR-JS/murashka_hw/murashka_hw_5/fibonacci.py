def fibonacci(n):
    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return a
