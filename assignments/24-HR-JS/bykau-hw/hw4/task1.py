text = input("Enter text: ")
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
        
sorted_words = sorted(counts, key=counts.get)
for word in sorted_words:
    print(f"{word}: {counts[word]}")
