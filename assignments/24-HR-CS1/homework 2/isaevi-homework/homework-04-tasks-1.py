text = input("Please write a text:")

words = text.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

def get_count(item):
    return item[1]



sorted_counts = sorted(counts.items(), key=get_count)

for word, count in sorted_counts:
    print(word, ":", count)