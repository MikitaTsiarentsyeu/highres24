import time
from functools import wraps

def Timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time.time()  
        result = func(*args, **kwargs)  
        endTime = time.time()  

        executionTime = endTime - startTime
        print(f"Function '{func.__name__}' executed in {executionTime:.6f} seconds.")
        
        return result  
    return wrapper

@Timer
def TestFunction():
    return sum(range(1000))

testResult = TestFunction()
print(testResult)