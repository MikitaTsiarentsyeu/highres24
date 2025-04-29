import time

def timer(f):
    def wrapper(list):
        start = time.time()
        result = f(list)
        return result, time.time() - start
    return wrapper

@timer
def sort_list(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

result, time = sort_list([5, 500, 4, 3, 46, 10, 1, 50, 108, 8, 26, 65, 9])
print(result, f"\n{time:.10f} seconds")