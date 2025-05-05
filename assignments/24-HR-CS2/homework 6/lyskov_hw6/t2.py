import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return end - start
    return wrapper

numbers = [1, 4, 5, 7, 8, 19, 42, 5, 2, 8]

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    for i in range(len(list)):
        print(list[i])

checkTime = timer(bubble_sort)
print(checkTime(numbers))
