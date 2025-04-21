def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)

#numbers
my_list = [6, -24, 24, 2141, 45253]
kick_out(my_list, 2141)
print(my_list) 