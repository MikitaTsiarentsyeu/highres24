def fib_gen(n):
    mem = {0: 0, 1: 1}
    
    def fib(k):
        if k not in mem:
            mem[k] = fib(k-1) + fib(k-2)
        return mem[k]
    
    for i in range(n):
        yield fib(i)
        
    
for num in fib_gen(30):
    print(num, end=" ")    
        