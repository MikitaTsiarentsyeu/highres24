from task2 import BubbleSort


UserText = input("Write any information: ")
lowUserText = UserText.lower().split()
count = {}


for i in lowUserText:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

words = list(count.keys())

textSorted = BubbleSort(words, count)

print("Sorted words and count: ")
for word in words:
    print(f"{word}: {count[word]} - thing(s)")