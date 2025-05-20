def fib_gen(n):
    memo = {}

    def fib(k):
        if k in memo:
            return memo[k]
        if k == 0:
            result = 0
        elif k == 1:
            result = 1
        else:
            result = fib(k - 1) + fib(k - 2)
        memo[k] = result
        return result

    for i in range(n):
        yield fib(i)

for number in fib_gen(10):
    print(number)