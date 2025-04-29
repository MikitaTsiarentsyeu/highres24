import string

text = input("Enter a text: ")

words = text.translate(str.maketrans('', '', string.punctuation)).split()

word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


sorted_word_count = sorted(word_count.items(), key=lambda x: x[1])

for word, count in sorted_word_count:
    print(f"{word}: {count}")
