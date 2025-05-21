def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)

#numbers
my_list = [6, -244, 24, 221, 45553]
kick_out(my_list, 221)
print(my_list) 