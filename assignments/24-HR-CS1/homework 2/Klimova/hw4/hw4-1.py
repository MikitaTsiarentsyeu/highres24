from collections import defaultdict
import re

def count_and_sort_words(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    words = cleaned_text.split()
    
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    
    sorted_counts = sorted(word_counts.items(), key=lambda item: item[1])
    
    return sorted_counts

user_text = input("Enter some text: ")

word_frequencies = count_and_sort_words(user_text)

print("\nWord frequencies (from least to most common):")
for word, count in word_frequencies:
    print(f"'{word}': {count}")