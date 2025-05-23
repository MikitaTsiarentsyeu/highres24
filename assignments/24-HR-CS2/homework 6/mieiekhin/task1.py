def custom_sort(iterable, key_func):
    items = list(iterable)
    n = len(items)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if key_func(items[j]) > key_func(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items

words = ['apple', 'banana', 'fig', 'cherry']
sorted_words = custom_sort(words, key_func=len)
print(sorted_words)