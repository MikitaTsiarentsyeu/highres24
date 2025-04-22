def custom_sort(iterable, key_func):
    lst = list(iterable)
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if key_func(lst[j]) > key_func(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

l = [2, 5, 6, 1, 3, 7]
print(custom_sort(l, lambda x: -x))