def fib_gen(n):
    memo = {}
    
    def fib_recursive(num):
        if num in memo:
            return memo[num]
        if num <= 1:
            memo[num] = num
        else:
            memo[num] = fib_recursive(num - 1) + fib_recursive(num - 2)
        return memo[num]
    
    for i in range(n):
        yield fib_recursive(i)

n = int(input())
for fib_num in fib_gen(n):
    print(fib_num)
