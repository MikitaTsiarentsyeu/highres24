import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start
        print(f"function '{func.__name__}' completed in {elapsed_time:.6f} second")
        return result
    return wrapper

@timer
def heavy_computation(n):
    return sum(i**2 for i in range(n))

if __name__ == '__main__':
    result = heavy_computation(100000)
    print("result:", result)