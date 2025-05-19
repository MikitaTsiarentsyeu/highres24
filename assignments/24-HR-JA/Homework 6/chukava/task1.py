def custom_sort(iterable, key_func):
    data = list(iterable)
    n = len(data)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if key_func(data[j]) < key_func(data[min_index]):
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

    return data

nums = [10, 3, 5, 8, 6, 7]
sorted_by_mod = custom_sort(nums, key_func=lambda x: x % 3)
print("Sorted by x % 3:", sorted_by_mod)