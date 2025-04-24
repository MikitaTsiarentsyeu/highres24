import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

@timer
def quick_function():
    return sum(range(1000))

@timer
def slow_function():
    time.sleep(2)
    return "Done!"

@timer
def intensive_computation(n):
    total = 0
    for i in range(n):
        total += sum(range(1000))
    return total


print(quick_function())
print(slow_function())
print(intensive_computation(1000))
