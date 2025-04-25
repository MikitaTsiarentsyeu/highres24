def custom_sort(iterable, key_func):
    items = list(iterable)

    for i in range(len(items)):
        for j in range(len(items) - 1):
            if key_func(items[j]) > key_func(items[j + 1]):
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
    return items


words = ["marshmallow", "chocolate", "cake", "donut", "caramel", "dragon", "wizard", "sword", "potion", "castle", "river", "mountain", "forest", "leaf", "cloud", "poem", "novel", "story", "epic", "tale", "pumpkin", "ghost", "witch", "candle", "midnight", "hope", "joy", "melancholy", "dream", "fear"]
sorted_words = custom_sort(words, key_func=len)
print(sorted_words)
