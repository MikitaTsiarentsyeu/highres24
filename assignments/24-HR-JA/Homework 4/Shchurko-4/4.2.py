l = [2, 56, 3, 2, 4, 56, 8, 9]

for i in range(len(l) - 1):
    min_index = i
    for j in range(i + 1, len(l)):
        if l[j] < l[min_index]:
            min_index = j
    if min_index != i:
        l[i], l[min_index] = l[min_index], l[i]

print(l)
