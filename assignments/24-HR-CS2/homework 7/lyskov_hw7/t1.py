def generate_fibonacci(n):
    memo = {} 

    def fibonacci(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            memo[k] = k 
        else:
            memo[k] = fibonacci(k - 1) + fibonacci(k - 2)  
        return memo[k]
  
    for i in range(n):
        yield fibonacci(i)

fib_count = 7 
for num in generate_fibonacci(fib_count):
    print(num, end=', ')
