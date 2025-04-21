def bubble_sort(iterable):
    for i in range(len(iterable)):
        for j in range(0, len(iterable) - i - 1):
            if iterable[j] > iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    return iterable

def custom_sort(iterable, key_func):
    return sorted(iterable, key=lambda x: key_func([x]))

inputList = input("Enter numbers, separated by spaces: ")
myList = [int(i) for i in inputList.split()]
sorted_numbers = custom_sort(myList, bubble_sort)
print(sorted_numbers)
