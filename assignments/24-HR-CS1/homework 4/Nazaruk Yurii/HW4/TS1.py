import string
from collections import Counter

text = input("Enter text: ")
words = []
for word in text.split():
    processed_word = word.strip(string.punctuation).lower()
    if processed_word:
        words.append(processed_word)
word_counts = Counter(words)
sorted_words = sorted(word_counts.items(), key=lambda item: (item[1], item[0]))
print(sorted_words)
