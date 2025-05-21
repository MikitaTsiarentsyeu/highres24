def custom_sort(iterable, key_func):
    items = list(iterable)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(items[j]) > key_func(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items

numbers = [5, 2, 9, 1]
sorted_numbers = custom_sort(numbers, key_func=lambda x: -x)
print(sorted_numbers) 