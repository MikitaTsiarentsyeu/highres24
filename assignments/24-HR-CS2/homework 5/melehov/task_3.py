def kick_out(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            l.pop(i)
        else:
            i += 1

my_list = [1, 2, 3, 2, 4, 2, 5]
kick_out(my_list, 2)
print(my_list)
