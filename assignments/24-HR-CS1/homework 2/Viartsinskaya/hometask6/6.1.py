def custom_sort(iterable, key_func):
    lst = list(iterable)
    for i in range(1, len(lst)):
        current = lst[i]
        current_key = key_func(current)
        j = i - 1
        while j >= 0 and key_func(lst[j]) > current_key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current
    return lst