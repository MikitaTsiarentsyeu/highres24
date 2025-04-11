def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swappped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swappped = True
                
        if not swappped:
            break
        
    return arr

arr = [23, 14, 53, 12, 10, 5, 2, 102, 14]

print(bubble_sort(arr))