def custom_sort(iterable, key_func):
    items = list(iterable)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if key_func(items[j]) < key_func(items[i]):
                items[i], items[j] = items[j], items[i]
    return items

words = ["waitress", "peacefully", "world", "monkey", "toy"]
sorted_words = custom_sort(words, key_func=len)
print(sorted_words)
