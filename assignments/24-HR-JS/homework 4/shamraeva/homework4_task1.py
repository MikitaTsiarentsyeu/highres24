text = input("Enter text: ")
words = text.strip().lower().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_counts = sorted(word_counts.items(), key=lambda item: item[1])

for word, count in sorted_counts:
    print(word, count)