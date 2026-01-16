def fib_recursive(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib_recursive(k - 1) + fib_recursive(k - 2)

def fib_gen(n):
    for i in range(n):
        yield fib_recursive(i)

for num in fib_gen(10):
    print(num)