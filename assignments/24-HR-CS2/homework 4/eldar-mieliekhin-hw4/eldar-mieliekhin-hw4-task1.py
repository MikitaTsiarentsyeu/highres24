userInput = input("Enter some text: ")

word_count = {}

for word in userInput.split(" "):
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_list = list(word_count.items())

n = len(word_list)

for i in range(n):
    for j in range(0, n - i - 1):
        if word_list[j][1] > word_list[j + 1][1]:
            word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]

for word, count in word_list:
    print(f"Слово '{word}' встречается {count} раз(а)")


            
        