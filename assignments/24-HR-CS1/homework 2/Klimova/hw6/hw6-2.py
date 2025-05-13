import time
from typing import Callable, Any, Tuple

def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"{func.__name__} executed in {duration:.6f} seconds")
        return result, duration
    return wrapper
