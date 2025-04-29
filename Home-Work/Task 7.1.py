def selection_sort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])

def custom_sort(iterable, key_func):
    return sorted(iterable, key=lambda x: key_func([x]))

input_list_of_nums = input("Enter numbers (with spaces): ")
list_of_nums = [int(i) for i in input_list_of_nums.split()]
sorted_nums = custom_sort(list_of_nums, selection_sort)
print(sorted_nums)