sorted = 0
array = list(map(int, input().split()))
len = len(array)

for i in range(len - 1):
    done = True
    for j in range(len-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            done = False
    if done:
        break
