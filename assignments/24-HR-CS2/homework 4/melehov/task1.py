import re

def count_and_sort_words(text):
    words = re.findall(r'\w+', text.lower())

    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    sorted_words = sorted(word_counts.items(), key=lambda item: (item[1], item[0]))

    return sorted_words

text = input("Enter some text: ")
word_counts = count_and_sort_words(text)

for word, count in word_counts:
    print(f"{word}: {count}")