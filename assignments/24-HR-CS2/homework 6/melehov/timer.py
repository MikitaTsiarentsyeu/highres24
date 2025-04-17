import time
from functools import wraps

def timer(print_time=True):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start

            if print_time:
                print(f"{func.__name__} took {elapsed:.6f}s")
            return (result, elapsed) if not print_time else result

        return wrapper

    return decorator


@timer(print_time=True)
def calculate_sum(n):
    return sum(range(n))

print(calculate_sum(1_000_000))
