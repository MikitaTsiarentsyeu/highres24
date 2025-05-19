from collections import Counter
import re

text = input("Enter text: ").lower()
words = re.findall(r'\w+', text)
counts = Counter(words)
for word, count in sorted(counts.items(), key=lambda x: (x[1], x[0])):
    print(word, ":", count)