def custom_sort(iterable, key_func):
    return sorted(iterable, key=lambda x: key_func([x]))
