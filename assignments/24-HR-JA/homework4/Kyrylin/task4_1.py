def count_words():
    text = input("Enter text: ")
    words = text.lower().split()
    
    word_counts = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1])

    for word, count in sorted_words:
        print(f"{word}: {count}")
count_words()
