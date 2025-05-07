def fib_gen(n):
    memo = {}

    def fib(k):
        if k == 0:
            return 0
        if k == 1:
            return 1
        if k in memo:
            return memo[k]
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    for i in range(n):
        yield fib(i)
