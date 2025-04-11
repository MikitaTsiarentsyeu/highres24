word_list = ["b", "c", "d", "a"]

n = len(word_list)
last_index = n - 1
while last_index > 0:
    new_last_index = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if word_list[j] < word_list[j + 1]:
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
                new_last_index = j
                swapped = True
        if swapped == False:
            break
    last_index = new_last_index
        
            
for word in word_list:
    print(word)