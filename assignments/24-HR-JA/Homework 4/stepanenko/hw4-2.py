num = list(map(int, input("Enter the numbers, plaese (for example: 1 2 3 4): ").split()))
for i in range(len(num)):
    for j in range(len(num) - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print(f"Sorted array: {num}")