numbers = input("Enter space-separated integers: ").strip().split()

if not all(n.isdigit() for n in numbers):
    print("Please enter only positive integers")
else:
    lst = list(map(int, numbers))
    n = len(lst)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break

    print("Sorted:", *lst)
