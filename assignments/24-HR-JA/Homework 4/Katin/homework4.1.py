words = {}
wordsList = []

text = input("Enter a text: ")

text = (text.lower().replace("!", "").replace("?", "").replace(".", "")
        .replace(",", "").replace(":", "").replace(";", "")
        .replace("-", "").replace('"', ""))

wordsList = text.split(" ");

for i in range(len(wordsList)):
    if wordsList[i] == '':
        continue
    if wordsList[i] in words:
        words[wordsList[i]] += 1
    else:
        words[wordsList[i]] = 1

wordsList = list(words.items())

for i in range(len(wordsList)):
    for j in range(len(wordsList) - 1):
        if wordsList[j][1] < wordsList[j + 1][1]:
            wordsList[j + 1], wordsList[j] = wordsList[j], wordsList[j + 1]

words = dict(wordsList)

print(words)





