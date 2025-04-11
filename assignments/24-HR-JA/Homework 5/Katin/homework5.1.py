def fibonacci(n:int) -> int:
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        n1 = 0
        n2 = 1
        n3 = 1
        for i in range(n-2):
            n3temp = n3
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3

print(fibonacci(3))

