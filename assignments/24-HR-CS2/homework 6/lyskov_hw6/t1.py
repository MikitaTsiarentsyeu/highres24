def bubble_sort(iterable, key_function):
    items = list(iterable)
    total_items = len(items)   
  
    for i in range(total_items - 1):
        for j in range(total_items - i - 1):
            if key_function(items[j]) > key_function(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items
words_list = ['apple', 'banana', 'fig', 'cherry']
sorted_words = bubble_sort(words_list, key_function=len)

print(sorted_words)
