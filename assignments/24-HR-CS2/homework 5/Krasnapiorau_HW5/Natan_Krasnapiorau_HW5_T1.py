def Fibonacci(n: int) -> int:
    if n <= 0:
        return "n must be a positive integer"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print(Fibonacci(-1))
print(Fibonacci(0))
print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))