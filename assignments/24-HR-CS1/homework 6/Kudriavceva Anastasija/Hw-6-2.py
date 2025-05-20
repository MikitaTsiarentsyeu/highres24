import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} sec")
        return result
    return wrapper  

@timer
def sum_numbers(n):
    return sum(range(n))

print(sum_numbers(4000000))