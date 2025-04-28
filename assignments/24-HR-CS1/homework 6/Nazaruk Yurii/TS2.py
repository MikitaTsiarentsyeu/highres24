import time
def timer(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    return result, f"{end_time - start_time} seconds"

@timer
def hello_world():
    time.sleep(1)  
    return "Hello, World!"

print(hello_world)