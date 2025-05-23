def remove_all_occurrences(lst, value):
    while value in lst:
        lst.remove(value)

my_list = [1, 2, 3, 2, 4, 2, 5]
remove_all_occurrences(my_list, 2)
print(my_list) 