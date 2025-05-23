def custom_sort(iterable, key_func):
    arr = list(iterable)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if key_func(arr[j]) > key_func(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

