import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"executed in {end_time - start_time} sec")
        return result
    return wrapper  

@timer
def sum_numbers(n):
    return sum(range(n))

print(sum_numbers(100000000))