def optimized_bubble_sort(arr):
    n = len(arr)
    while n > 1:
        last_swap = 0
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                last_swap = i
                swapped = True
                n = last_swap

                if not swapped:
                    break

                return arr
            