text = input("Введите текст: ")
words = text.lower().split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


word_list = list(word_counts.items())
n = len(word_list)
for i in range(n):
    for j in range(n - i - 1):
        if word_list[j][1] > word_list[j + 1][1]:
            word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]

for word, count in word_list:
    print(f"{word} : {count}")