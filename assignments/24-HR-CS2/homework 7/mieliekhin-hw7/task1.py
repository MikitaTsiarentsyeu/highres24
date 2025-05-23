def fib(n):
    memo = {}
    
    for i in range(n):
        if i not in memo:
            if i <= 1:
                memo[i] = i
            else:
                memo[i] = memo[i - 1] + memo[i - 2]
        yield memo[i]

for i in fib(10):
    print(i)
