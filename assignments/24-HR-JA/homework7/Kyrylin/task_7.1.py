def fib_gen(n):
    fibonacci_dict = {0: 0, 1: 1}

    def fibonacci(k):
        if k in fibonacci_dict:
            return fibonacci_dict[k]
        else:
            result = fibonacci(k - 1) + fibonacci(k - 2)
            fibonacci_dict[k] = result
            return result

    for i in range(n):
        yield fibonacci(i)

print(list(fib_gen(20)))
