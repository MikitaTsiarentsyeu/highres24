def custom_sort(iterable, key_func):
    data = list(iterable)
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and key_func(data[j]) > key_func(current):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
    return data

words = ["waitress", "peacefully", "world", "monkey", "toy"]
sorted_words = custom_sort(words, key_func=len)
print(sorted_words)
