def fib_gen(n):
    memo = {}

    def fib(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            memo[k] = k
        else:
            memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    for i in range(n):
        yield fib(i)


fib_num = 7
for num in fib_gen(fib_num):
    print(num, end=', ')
