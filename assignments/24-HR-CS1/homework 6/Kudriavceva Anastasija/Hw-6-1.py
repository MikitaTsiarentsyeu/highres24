def custom_sort(iterable, key_func):
    arr = list(iterable)
    keys = [key_func(item) for item in arr]
    for i in range(1, len(arr)):
        key_item = arr[i]
        key_value = keys[i]
        j = i - 1
        while j >= 0 and keys[j] > key_value:
            arr[j + 1] = arr[j]
            keys[j + 1] = keys[j]
            j -= 1
        arr[j + 1] = key_item
        keys[j + 1] = key_value
    return arr