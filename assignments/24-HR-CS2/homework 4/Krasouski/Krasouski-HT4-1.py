from collections import Counter

userInput = input()
l = userInput.split(" ")

print(l)

counter = Counter(l)
l.sort(key=lambda x: counter[x], reverse=True)

print(l)