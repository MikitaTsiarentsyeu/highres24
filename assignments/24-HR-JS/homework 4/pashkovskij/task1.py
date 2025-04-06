# delete all dots and commas from the text and count the number of words in the text
import string

text = input("Enter a text: ")
# Remove punctuation from words
words = text.translate(str.maketrans('', '', string.punctuation)).split()

word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_word_count)
