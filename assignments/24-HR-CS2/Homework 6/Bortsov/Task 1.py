def custom_sort(iterable, key_func):
    items = list(iterable)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(items[j]) > key_func(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

List_Words = ["Cs", "Dota", "Fifa", "Cyberpunk", "Minecraft"]
sorted_Words = custom_sort(List_Words, key_func=len)
print(sorted_Words)
