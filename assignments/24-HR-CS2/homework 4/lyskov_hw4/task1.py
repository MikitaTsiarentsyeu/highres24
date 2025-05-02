import string
from collections import Counter

text = input("Enter some text: ")
words = text.split()
clean_words = []

for w in words:
    w = w.lower()
    w = w.strip(string.punctuation)
    if w != "":
        clean_words.append(w)

counts = Counter(clean_words)

# сортировка по количеству, затем по алфавиту
sorted_list = sorted(counts.items(), key=lambda x: (x[1], x[0]))

print("Words and their counts:")
print(sorted_list)
