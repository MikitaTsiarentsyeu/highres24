import time
from functools import wraps

# Decorator that prints execution time
def timer_print(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} took {duration:.4f} seconds")
        return result
    return wrapper

# Example usage
@timer_print
def wait(seconds):
    time.sleep(seconds)

@timer_print
def sum_range(n):
    return sum(range(n))

wait(1)         # Prints: "wait took 1.0001 seconds"
sum_range(10**6) # Prints: "sum_range took 0.0253 seconds"