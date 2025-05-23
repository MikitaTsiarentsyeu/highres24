import time
from math import sin

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        print(f"func {func.__name__} runs for {exec_time:.3f} seconds")
        return result
    return wrapper


@timer
def foo():
    total = 0
    for i in range(1000000):
        total += sin(i)
    return total

foo()