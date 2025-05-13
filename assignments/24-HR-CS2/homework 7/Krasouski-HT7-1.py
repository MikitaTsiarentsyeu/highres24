import time

def timerDecorator(func): # decorator that prints operation time value
    def wrapper():
        start_time = time.time()
        func()  
        end_time = time.time()
        
        print (end_time - start_time)
    return wrapper

@timerDecorator
def someFunc():
    def fibonacci(n, a = 0, b = 1):
        if n == 0:
            return
        yield a
        yield from fibonacci(n - 1, b, a + b)

    for num in fibonacci(amount):
        print(num)

amount = int(input("How much fibonachi nums do you need? ")) # no text or negative value validation
someFunc()