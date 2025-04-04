text = input("Type your text: ")

words = text.lower().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda item: item[1])

print("Word counts sorted:")
for word, count in sorted_words:
    print(word, ":", count)