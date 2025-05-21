def fib_gen(n):
    mem = {}

    def fib(i):
        if i in mem:
            return mem[i]
        
        elif i <= 1:
            mem[i] = i
            return i

        else:
            mem[i] = fib(i - 1) + fib(i - 2)
            return mem[i]

    for i in range(n):
        yield fib(i)

for x in fib_gen(5):
    print(x)
