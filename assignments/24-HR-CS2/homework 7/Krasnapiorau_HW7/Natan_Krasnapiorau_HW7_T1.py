def FibGen(n):
    memo = {}
    
    def Fib(i):
        if i in memo:
            return memo[i]
        if i <= 1:
            memo[i] = i
        else:
            memo[i] = Fib(i - 1) + Fib(i - 2)
        return memo[i]

    for i in range(n):
        yield Fib(i)

for num in FibGen(10):
    print(num, end=' ')