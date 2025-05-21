def count_words(text):
    words = text.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    sorted_counts = sorted(counts.items(), key=lambda item: item[1])

    for word, count in sorted_counts:
        print(word, ":", count)

