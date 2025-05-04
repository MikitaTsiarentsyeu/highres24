def fib_gen(n, memo=None):
    if memo is None:
        memo = {}

    def fib_recursive(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            memo[k] = k
        else:
            memo[k] = fib_recursive(k - 1) + fib_recursive(k - 2)
        return memo[k]

    for i in range(n):
        yield fib_recursive(i)

for num in fib_gen(10):
    print(num)