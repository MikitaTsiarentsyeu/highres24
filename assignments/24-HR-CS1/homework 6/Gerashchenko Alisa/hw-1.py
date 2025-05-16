def custom_sort(iterable, key_func):
    item = list(iterable)
    a = len(item)
    for i in range(a):
        for j in range(0, a - i - 1):
            if key_func(item[j]) > key_func(item[j + 1]):
                item[j], item[j + 1] = item[j + 1], item[j]
    return item

num = [3, 11, 7, 4, 31, 1]
print(custom_sort(num, key_func = lambda x: -x))