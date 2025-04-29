def fib_gen(n):
    memo = {}

    def fib(i):
        if i in memo:
            return memo[i]
        if i == 0:
            memo[i] = 0
        elif i == 1:
            memo[i] = 1
        else:
            memo[i] = fib(i - 1) + fib(i - 2)
        return memo[i]

    i = 0
    while i < n:
        yield fib(i)
        i += 1

for num in fib_gen(10):
    print(num)
