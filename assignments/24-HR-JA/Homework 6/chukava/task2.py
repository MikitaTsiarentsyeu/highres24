import time

def functiontimer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds")
        return result
    return wrapper

@functiontimer
def quick_sum():
    total = sum(range(10000))
    print("Sum:", total)

@functiontimer
def sort_big_list():
    lst = [i for i in range(500000, 0, -1)]
    lst.sort()
    print("First 3 items:", lst[:3])

@functiontimer
def wait_task():
    time.sleep(2)
    print("Waited for 2 seconds")

quick_sum()
sort_big_list()
wait_task()