import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return {
            "result": result,
            "execution_time": elapsed_time
        }
    return wrapper
#Slow function
@timer
def slow_function():
    time.sleep(2)
    return "Slow function end!"
#Fast function
@timer
def fast_function():
    return sum(range(1000)) 

#Using decorator
slow_output = slow_function()
fast_output = fast_function()

print("Result slow func:", slow_output["result"])
print("Slow function execution time:", slow_output["execution_time"], "second")

print("Quick function result:", fast_output["result"])
print("Fast function execution time:", fast_output["execution_time"], "second")
