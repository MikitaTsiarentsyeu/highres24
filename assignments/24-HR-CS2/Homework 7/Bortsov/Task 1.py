def fib_gen(n):
    dicti = {0: 0, 1: 1}
    def fib(k):
        if k in dicti:
            return dicti[k]
        dicti[k] = fib(k - 1) + fib(k - 2)
        return dicti[k]

    for i in range(n):
        yield fib(i)
        
for num in fib_gen(10):
    print(num)
