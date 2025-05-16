def fib_gen(n):
    mem = {}

    def fib(i):
        if i in mem:
            return mem[i]
        if i <= 1:
            mem[i] = i
        else:
            mem[i] = fib(i - 1) + fib(i - 2)
        return mem[i]

    for i in range(n):
        yield fib(i)


for num in fib_gen(5):
    print(num, end=' ')
