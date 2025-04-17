import time

def timer(func):
    def wrapper(*arg, **kwarg):

        start = time.perf_counter()
        func(*arg, **kwarg)
        endl = time.perf_counter()
        difr = endl - start
        print(f"{func.__name__}, time:{difr:.6f} seconds")
        return func(*arg, **kwarg)
    return wrapper

@timer
def printer():
    return "ddd"

@timer
def sleepFunction():
    time.sleep(1)

@timer
def Multiply():
    return 20**2 * 20321

sleepFunction()
printer()
print(Multiply())
