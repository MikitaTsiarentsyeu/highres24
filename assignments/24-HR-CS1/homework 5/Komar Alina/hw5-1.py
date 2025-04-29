def fibonacci(n: int) -> int:
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b
num = int(input("Enter a number for fibonacci sequence: "))
print(fibonacci(num))