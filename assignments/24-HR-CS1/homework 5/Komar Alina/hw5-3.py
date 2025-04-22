def kick_out(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            l.pop(i)
        else:
            i += 1

input_list_of_nums = input("Enter numbers (with spaces): ")
list_of_nums = [int(i) for i in input_list_of_nums.split()]
num_to_pop = int(input("Enter num to remove: "))
kick_out(list_of_nums, num_to_pop)
print(list_of_nums)