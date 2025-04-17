def kick_out(l: list, val: object) -> None:
    new_list = []
    for item in l:
        if item != val:
            new_list.append(item)
    l.clear()
    l.extend(new_list)

my_list = [1, 2, 3, 2, 4, 2, 5]
value_to_remove = 2
kick_out(my_list, value_to_remove)
print(f"List after deletion {value_to_remove}: {my_list}")