def custom_sort(iterable, key_func):
    items = list(iterable)

    n = len(items)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if key_func(items[j]) < key_func(items[i]):
                min_index = j
                items[i], items[min_index] = items[min_index], items[i]

    return items

words = ['banana', 'apple', 'kiwi', 'cherry']
sorted_words = custom_sort(words, len)
print(sorted_words)
nums = [10, 3, 6, 1, 7]
sorted_nums = custom_sort(nums, lambda x:x)
print(sorted_nums)