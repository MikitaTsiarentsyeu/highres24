import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time:", round(end - start, 6), "seconds")
        return result
    return wrapper
@timer
def slow_function():
    time.sleep(1.5)
    return "Done"

@timer
def count_to_million():
    return sum(range(1_000_000))
print(slow_function())
print(count_to_million())
