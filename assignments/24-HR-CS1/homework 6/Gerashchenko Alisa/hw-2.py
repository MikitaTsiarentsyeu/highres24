import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        return result, f"{end - start:.2f} sec"
    return wrapper

@timer
def hello_world():
    time.sleep(1)
    return "Bebe"

@timer
def summ():
    time.sleep(1)
    return sum(range(100))

print(hello_world())
print(summ())
