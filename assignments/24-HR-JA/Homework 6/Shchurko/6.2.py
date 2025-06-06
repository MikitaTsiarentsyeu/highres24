import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Function '{func.__name__}' executed in {duration:.6f} seconds")
        return result

    return wrapper


@timer
def custom_sort_bubble(iterable, key_func):
    l = list(iterable)
    n = len(l)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(l[j]) > key_func(l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


@timer
def custom_sort_selection(iterable, key_func):
    l = list(iterable)
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if key_func(l[j]) < key_func(l[min_index]):
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l


data = ['apple', 'banana', 'kiwi', 'pear']

sorted_bubble = custom_sort_bubble(data, key_func=len)
sorted_selection = custom_sort_selection(data, key_func=len)

print("Bubble Sort:", sorted_bubble)
print("Selection Sort:", sorted_selection)
