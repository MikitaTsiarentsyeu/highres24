def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            
            break
    return a


lst = [341, 325, 25, 64, 18, 21, 19,24,24334,343434,353545,4554654,2234234,54,54,21,327,343,2124,3456,3253,1111,0,3421,211111111,4444444444443,124,1414,1214,23,32]
print("Отсортировано:", bubble_sort(lst))