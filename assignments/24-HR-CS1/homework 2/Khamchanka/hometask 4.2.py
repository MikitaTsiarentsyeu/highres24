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
numbers = [23, 21, -250, 102, 15.1, -169.9, 28]
print("Sorted array:", bubble_sort(numbers))