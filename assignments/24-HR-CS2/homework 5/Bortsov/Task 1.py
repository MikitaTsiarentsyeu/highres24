def fibonacci(n: int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    first = 0
    second = 1
    for i in range(3, n + 1):
        nextNum = first + second
        first = second
        second = nextNum
    return nextNum
print(fibonacci(5))