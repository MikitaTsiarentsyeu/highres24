import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def fast():
    sum(range(1000))

@timer
def slow():
    time.sleep(1)

@timer
def medium():
    for _ in range(10**6):
        pass

fast()
slow()
medium()