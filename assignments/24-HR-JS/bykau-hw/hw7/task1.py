def fib_gen(n):
    memo = {0: 0, 1: 1}
    
    def fib(k):
        if k in memo:
            return memo[k]
        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    
    for i in range(n):
        yield fib(i)


for num in fib_gen(50):
    print(num)
