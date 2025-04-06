from collections import Counter

def countAndSortWords(text):

    words = text.lower().split()
    words = [word.strip(".,!?;:\"'()[]{}") for word in words]
    wordCounts = Counter(words)
    sortedWords = sorted(wordCounts.items(), key=lambda x: x[1])
    
    for word, count in sortedWords:
        print(f"{word}: {count}")

countAndSortWords(input("Enter your text: "))