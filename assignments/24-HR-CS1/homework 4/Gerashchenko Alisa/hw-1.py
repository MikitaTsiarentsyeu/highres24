text = input("Enter some text by space: ")
words = text.lower().split()

word_arr = []

for word in words:
    found = False
    for a in word_arr:
        if a[0] == word:
            a[1] += 1
            found = True
            break
    if not found:
        word_arr.append([word, 1])

n = len(word_arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if word_arr[j][1] > word_arr[j + 1][1]:
            word_arr[j], word_arr[j + 1] = word_arr[j + 1], word_arr[j]

for word, count in word_arr:
    print(word + ": " + str(count))