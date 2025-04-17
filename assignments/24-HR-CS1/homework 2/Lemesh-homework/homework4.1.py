text = input("Enter your text: \n")
words = text.lower().split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1])

for word, count in sorted_word_counts:
    print(f"{word}: {count}")

