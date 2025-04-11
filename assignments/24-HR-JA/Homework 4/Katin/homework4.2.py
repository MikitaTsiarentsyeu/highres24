list = [54, 62, 804, 7, 4, 52, 1002, 41, 67, 1, 0]

for i in range(len(list)):
    minIndex = i;
    for j in range(i + 1, len(list)):
        if list[minIndex] > list[j]:
            minIndex = j;
    list[i], list[minIndex] = list[minIndex], list[i]

print(list)
