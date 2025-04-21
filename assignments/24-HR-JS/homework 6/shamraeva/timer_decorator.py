import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        return result, duration
    return wrapper


#check
if __name__ == "__main__":
    @timer
    def fast_function():
        return sum(range(1000))

    @timer
    def slow_function():
        total = 0
        for i in range(10**6):
            total += i
        return total

    @timer
    def sleep_function():
        import time
        time.sleep(1)
        return "done"

    res_fast, time_fast = fast_function()
    print(res_fast, time_fast > 0)

    res_slow, time_slow = slow_function()
    print(res_slow, time_slow > 0)

    res_sleep, time_sleep = sleep_function()
    print(res_sleep, round(time_sleep) == 1)
