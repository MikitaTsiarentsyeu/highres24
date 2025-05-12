def custom_sort(iterable, key_func):
    lisst = list(iterable)
    n = len(lisst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(lisst[j]) > key_func(lisst[j + 1]):
                lisst[j], lisst[j + 1] = lisst[j + 1], lisst[j]
    return lisst
