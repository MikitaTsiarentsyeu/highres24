import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнена за {end - start} секунд")
        return result
    return wrapper

@timer
def slow_function():
   time.sleep(3)
    
@timer
def mid_function():
    i = 0
    while(i < 10000):
        i += 1 
        print(i)

@timer
def fast_function():
    1+1

slow_function()
mid_function()
fast_function()
