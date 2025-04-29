def custom_sort(iterable, key_func):
    return sorted(iterable, key=key_func)

print(custom_sort([1, 2, 3, 4, 44, 35, 21, 32, 87], lambda x: x % 2 == 0))   