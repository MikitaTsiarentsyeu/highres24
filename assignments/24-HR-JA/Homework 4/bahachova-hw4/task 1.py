text = input("Enter some text: ")
text = text.lower()
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda item: item[1])

for word, count in sorted_words:
    print(word, ":", count)