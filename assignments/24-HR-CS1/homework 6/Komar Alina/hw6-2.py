import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        return {
            'result': result,
            'time': duration
        }
    return wrapper


@timer
def exponentiate(x, y):
    return x ** y

@timer
def sleep_funct():
    time.sleep(2)
    return True

checker = exponentiate(7, 51)
print(checker)

checker = sleep_funct()
print(checker)