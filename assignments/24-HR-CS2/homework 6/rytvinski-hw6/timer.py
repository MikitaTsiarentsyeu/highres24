import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        exec_time = end - start
        
        print(f"Function '{func.__name__}' was executed in {exec_time:.4f} seconds")

        return result
    
    return wrapper


@timer
def operation():
    total = 0
    
    for i in range(1_000_000):
        total += i
        
    return total


operation()