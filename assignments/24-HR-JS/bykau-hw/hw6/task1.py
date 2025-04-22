def custom_sort(iterable, key_func):
    for i in range(len(iterable)):
        for j in range(len(iterable) - i - 1):
            if key_func(iterable[j]) > key_func(iterable[j + 1]):
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    return iterable
    
num = [12, 45, 3, 78, 23, 9, 4, 100, 63, 1]
print(custom_sort(num, lambda x: x))