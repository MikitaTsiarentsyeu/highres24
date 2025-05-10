def fib_gen(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}
    if n <= 0:
        return
    elif n == 1: 
        yield memo[0]
    else:
        yield from fib_gen(n - 1, memo)
        k = n - 1
        if k not in memo:
            memo[k] = memo[k - 1] + memo[k - 2]
        yield memo[k]