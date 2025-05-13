def custom_sort(iterable, key_func):
    data = list(iterable)
    n = len(data)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(data[j]) > key_func(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
