import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Функция '{func.__name__}' выполнена за {elapsed:.3f} секунд")
        return result
    return wrapper
