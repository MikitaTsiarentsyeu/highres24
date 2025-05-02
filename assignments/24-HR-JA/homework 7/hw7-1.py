def fib_gen(n):
    memo = {}  

    def _fib(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            return k
        else:
            result = _fib(k - 1) + _fib(k - 2)
            memo[k] = result
            return result

    for i in range(n):
        yield _fib(i)


print("The first 10 Fibonacci numbers:")
for num in fib_gen(10):
    print(num)

print("-" * 20)