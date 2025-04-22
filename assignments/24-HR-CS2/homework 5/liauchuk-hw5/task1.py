def fibonacci(x: int) -> int:
    a, b = 1, 1
    for i in range(1, x + 1):
        if(i == x):
            print(a)
        a, b = b, a + b


fibonacci(12)