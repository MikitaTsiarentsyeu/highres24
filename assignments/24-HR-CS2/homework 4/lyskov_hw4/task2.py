words = ["b", "c", "d", "a"]

length = len(words)

i = 0
while i < length:
    j = 0
    while j < length - 1:
        if words[j] < words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp
        j += 1
    i += 1

for w in words:
    print(w)
