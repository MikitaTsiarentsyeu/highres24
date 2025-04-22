import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"The function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

@timer
def fast_function(n):
    sum(range(n + 1))

@timer
def another_slow_function(text):
    for _ in text * 100000:
        pass

slow_function()
fast_function(1000000)
another_slow_function("Example")