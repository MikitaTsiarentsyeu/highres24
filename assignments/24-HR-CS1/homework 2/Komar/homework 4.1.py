def count_words_in_text(text):
    words = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text).split()
    word_counts = {}
    for text_word in words:
        if text_word in word_counts:
            word_counts[text_word] += 1
        else:
            word_counts[text_word] = 1
    sorted_word_count = sorted(word_counts.items(), key=lambda item: item[1])
    return sorted_word_count


user_input = input("Enter text to count words: ")
result = count_words_in_text(user_input)
for word, count in result:
    print(f"{word}: {count}")
