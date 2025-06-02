def custom_sort(iterable, key_func):
    items = list(iterable)

    for i in range(len(items)):
        for j in range(len(items) - 1):
            if key_func(items[j]) > key_func(items[j + 1]):
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
    return items


words = ["speed", "engine", "driver", "podium", "finish", "lap", "circuit", "champion", "victory", "checkered", "turbo", "accelerate", "brake", "overtake", "pitstop", "rally", "dragster", "formula", "gears", "tires", "racecar", "track", "flag", "start", "sprint", "marathon", "velocity", "nitro", "pedal", "motor"]
sorted_words = custom_sort(words, key_func=len)
print(sorted_words)
