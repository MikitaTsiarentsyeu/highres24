def fib_gen(n:int):
    memo = {0: 0, 1: 1}
    def fib(n, memo={0: 0, 1: 1}):
        if n in memo:
            return memo[n]
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]
    i = 0
    while i < n + 1:
        memo[i] = fib(i, memo)
        yield memo[i]
        i += 1
for i in fib_gen(5):
    print(i)