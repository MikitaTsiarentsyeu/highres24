def custom_sort(iterable, key_func):
    arr = list(iterable)
    for i in range(1, len(arr)):
        key_item = arr[i]
        key_value = key_func(key_item)
        j = i - 1
        while j >= 0 and key_func(arr[j]) > key_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr
