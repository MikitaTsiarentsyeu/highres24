import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("function:", func.__name__)
        print("time taken:", end - start, "seconds")
        return result
    return wrapper

@timer
def wait_two_seconds():
    time.sleep(2)
    return "finished"

@timer
def add_numbers():
    total = 0
    for i in range(1000000):
        total += i
    return total

print(wait_two_seconds())
print(add_numbers())
