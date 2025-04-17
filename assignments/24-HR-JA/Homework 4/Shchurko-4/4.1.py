from collections import Counter
import string

text = input("Enter your text: ")
cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation)).strip(".,!?;:-()[]{}\"'")
words = cleaned_text.split()
word_counts = Counter(words)
sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1])
for word, count in sorted_word_counts:
    print(f"{word}: {count}")
