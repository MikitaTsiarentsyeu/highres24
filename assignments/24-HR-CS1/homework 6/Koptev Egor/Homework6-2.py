import time
import random

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() #Record Start Time
        result = func(*args, **kwargs)  #Call our funct
        end_time = time.time()  #Record End time
        execution_time = end_time - start_time  #Calc exec time
        print(f"Func '{func.__name__}' exec for {execution_time:.6f} seconds.")
        return result
    return wrapper

@timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

array = [random.randint(1, 1000) for _ in range(100)]
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)