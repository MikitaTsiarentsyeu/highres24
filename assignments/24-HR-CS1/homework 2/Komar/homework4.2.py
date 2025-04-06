def bubble_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        swapped = False
        for j in range(0, arr_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


text = input("Input array (with space): ")
nums = list(map(int, text.split()))
bubble_sort(nums)
print("Sorted array:", nums)
