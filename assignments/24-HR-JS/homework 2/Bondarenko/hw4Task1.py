text = input("Введите текст: ")

words = text.lower().split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: (x[1], x[0]))

print("Слова и их частота (от менее частых к более частым):")
for word, count in sorted_words:
    print(f"{word}: {count}")