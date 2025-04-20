def fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
n = int(input())
print(fibonacci(n))