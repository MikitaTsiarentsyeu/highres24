def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        completed = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                completed = True
        if not completed:
            break
    return arr

#Numbers to test
numbers = [23, 34, -25, -12, 222.8, 241.6, 13]
print("Sorted array:", bubble_sort(numbers))