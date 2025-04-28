import re
from collections import Counter

def count_word_occurrences(text):
    words = re.findall(r"\b[\w'-]+\b", text.lower())
    words = [word for word in words if word.isalpha() or ("'" in word) or ('-' in word)]
    word_counts = Counter(words)
    sorted_counts = sorted(word_counts.items(), key=lambda x: (x[1], x[0]))
    return sorted_counts

# Get text from user input
user_input = input("Enter your text: ")

# Process and count words
result = count_word_occurrences(user_input)

# Display results
print("\nResults (from least to most frequent):")
for word, count in result:
    print(f"'{word}': {count} occurrence{'s' if count > 1 else ''}")