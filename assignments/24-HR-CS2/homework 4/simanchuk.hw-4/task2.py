def BubbleSort(words, count):
    for i in range(len(words)):
        for j in range(len(words) - 1 - i):
            if count[words[j]] > count[words[j + 1]]:
                words[j], words[j + 1] =  words[j + 1], words[j]