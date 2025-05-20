def fib_gen(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be non-negative integer")
    
    cache = {0: 0, 1: 1}
    
    def fib(k):
        if k not in cache:
            cache[k] = fib(k-1) + fib(k-2)
        return cache[k]
    
    for i in range(n):
        yield fib(i)

# Example
print(list(fib_gen(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]