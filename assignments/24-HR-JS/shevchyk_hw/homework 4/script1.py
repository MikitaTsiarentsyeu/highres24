from collections import Counter
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return sorted(word_counts.items(), key=lambda x: x[1])


text = "This a test. This is only a test! This test is a test?"
print(count_words(text))