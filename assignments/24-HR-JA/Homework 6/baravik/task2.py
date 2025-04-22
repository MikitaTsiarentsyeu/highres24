import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        return result, elapsed
    return wrapper

@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

@timer
def fast_op():
    return sum(range(100))

@timer
def sleep_op():
    time.sleep(2)
    return "Done"

result, elapsed = slow_sum(10**6)
print(f"Result: {result}, Time: {elapsed:.4f} sec")
result2, time2 = fast_op()
print(f"Result: {result2}, Time: {time2:.4f} sec")
result3, time3 = sleep_op()
print(f"Result: {result3}, Time: {time3:.4f} sec")