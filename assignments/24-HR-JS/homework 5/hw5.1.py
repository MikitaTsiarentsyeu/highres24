def fibonacci(n: int, z={0: 0, 1: 1}) -> int:
    if n in z:
        return z[n]
    x = fibonacci(n - 1, z)
    y = fibonacci(n - 2, z)
    z[n] = x + y
    return z[n]
print(fibonacci(10))
