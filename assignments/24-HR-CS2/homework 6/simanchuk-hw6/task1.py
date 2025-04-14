def custom_sort(iterable, key_func):
    item = list(iterable)

    for i in range(len(item)):
        for j in range(len(item) - 1 - i):
            if key_func(item[j]) > key_func(item[j + 1]):
                item[j], item[j + 1] =  item[j + 1], item[j]
    return item

words = ["pom", "pifpaf", "ppppppp"]

print(custom_sort(words, key_func=len))
