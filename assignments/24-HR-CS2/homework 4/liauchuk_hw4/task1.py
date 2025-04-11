from task2 import bubble_sort

text = input("input here: ").lower().split()
count = {}
for i in text:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
words = list(count.keys())
text_sorted = bubble_sort(words, count)
for word in words:
    print(f"{word}: {count[word]}")