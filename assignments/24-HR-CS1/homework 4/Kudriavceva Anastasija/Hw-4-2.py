def bubble_sort(arr):
    n = len(arr)
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                new_n = i
        n = new_n 

text = input("Input array (with space): ")
nums = list(map(int, text.split()))
bubble_sort(nums)
print("Sorted array:", nums)
