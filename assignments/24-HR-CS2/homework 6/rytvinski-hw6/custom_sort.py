def custom_sort(iterable, key_func):
    items = list(iterable) 
    n = len(items)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if key_func(items[j]) > key_func(items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
    
    return items

l = [3, 2, 6, 19, 20, 13, 7, 5]
print(custom_sort(l, lambda x: -x))