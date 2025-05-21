fibonacciDictionary = {};

fibonacciDictionary[0] = 0;
fibonacciDictionary[1] = 1;

def fib_gen(n):

    def fibonacci(n):
        if n in fibonacciDictionary:
            return fibonacciDictionary[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            fibonacciDictionary[n] = result
            return result

    for i in range(n + 1):
        yield fibonacci(i)

print(list(fib_gen(19)))
print(fibonacciDictionary)


