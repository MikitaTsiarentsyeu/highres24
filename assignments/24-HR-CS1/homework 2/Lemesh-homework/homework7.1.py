def fib_gen(n):
    memo = {}
    
    def fib_recursive(x):
        if x in memo:
            return memo[x]
        if x <= 1:
            memo[x] = x
        else:
            memo[x] = fib_recursive(x - 1) + fib_recursive(x - 2)
        return memo[x]

    for i in range(n):
        yield fib_recursive(i)

# Example
for fib in fib_gen(50):
    print(fib)