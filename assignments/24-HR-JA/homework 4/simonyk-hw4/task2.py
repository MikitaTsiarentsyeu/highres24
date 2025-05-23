text = input("Type an array with numbers separated by space: ")
arr = list(map(int, text.split()))

n = len(arr)
for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array:", arr)