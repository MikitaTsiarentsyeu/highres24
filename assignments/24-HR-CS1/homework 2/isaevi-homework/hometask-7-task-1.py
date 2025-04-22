def fib_gen(n):
    memo = {}
    
    def fib(k):
        if k in memo:
            return memo[k]
        if k < 2:
            memo[k] = k
            return k
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]
    
    for i in range(n):
        yield fib(i)

if __name__ == "__main__":
    n = 10
    for num in fib_gen(n):
        print(num)
