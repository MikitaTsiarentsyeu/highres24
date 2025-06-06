def fib_gen(n):
    memo = {}
    def fib(i):
        if i in memo:
            return memo[i]
        if i == 0:
            memo[0] = 0
        elif i == 1:
            memo[1] = 1
        else:
            memo[i] = fib(i - 1) + fib(i - 2)
        return memo[i]
    for i in range(n):
        yield fib(i)

for num in fib_gen(8):
    print(num)
