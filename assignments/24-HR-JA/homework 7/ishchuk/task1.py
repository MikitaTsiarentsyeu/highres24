def fib_gen(n):
    memo = {0: 0, 1: 1}

    def fib(x):
        if x in memo:
            return memo[x]
        result = fib(x - 1) + fib(x - 2)
        memo[x] = result
        return result

    i = 0
    while i <= n:
        yield fib(i)
        i += 1

for number in fib_gen(5):
    print(number)
