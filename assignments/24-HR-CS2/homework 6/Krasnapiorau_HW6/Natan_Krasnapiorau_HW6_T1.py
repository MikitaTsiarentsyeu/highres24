def CustomSort(iterable, keyFunc):
    arr = list(iterable)  
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if keyFunc(arr[j]) > keyFunc(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


data = ["apple", "banana", "cherry", "date"]
sortedByLength = CustomSort(data, keyFunc=len)
print("Sorted by length:", sortedByLength)

nums = [3, 11, 9, 2, 14, 10]
sortedByCloseness = CustomSort(nums, keyFunc=lambda x: abs(x - 10))
print("Sorted by closeness to 10:", sortedByCloseness)