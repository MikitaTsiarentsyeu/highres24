def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted: #Sorted = true -> array already sorted
            print("Sorted array:", end=" ")
            break
    return arr

array = [142, 454, 24, 1, 252, 456, 424, 416]
sorted_arr = optimized_bubble_sort(array)

for i in sorted_arr:
    print(i, end=" ")