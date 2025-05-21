def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1
    count = 2
    while count < n:
        c = a + b
        a = b
        b = c
        count += 1

    return b

print(fibonacci(3))
