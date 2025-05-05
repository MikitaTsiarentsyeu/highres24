def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print("Исходный список:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", sorted_numbers)