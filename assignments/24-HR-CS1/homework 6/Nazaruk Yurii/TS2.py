import time
def timer(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    return result, f"{end_time - start_time} seconds"

def hello_world():
    time.sleep(10)  
    return "Hello, World!"

print(timer(hello_world))