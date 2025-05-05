#i could not find a way to use yield from

known = {0: 0, 1: 1}
def fib_gen(n):
    for i in range(n):
        if i in known:
            yield known[i]
        else:
            known[i] = list(fib_gen(i)).pop() + list(fib_gen(i - 1)).pop()
            yield known[i]

for i in fib_gen(40):
    print(i)