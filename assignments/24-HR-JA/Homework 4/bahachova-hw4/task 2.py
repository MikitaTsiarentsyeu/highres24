numbers = [5, 2, 9, 1, 5, 6]
n = len(numbers)
for i in range(n):
    swapped = False

    for j in range(0, n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

    if not swapped:
        break

print("Sorted list:", numbers)