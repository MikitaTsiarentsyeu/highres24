import re


def count_words(s):
    clean_text = re.sub(r"[^\w\s']", '', s.lower())
    words = clean_text.split()
    
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    sorted_counts = sorted(word_counts.items(), key=lambda item: item[1])
    
    return sorted_counts


s = input("Input string: ")
result = count_words(s)

for word, count in result:
    print(f"{word}: {count}")
    