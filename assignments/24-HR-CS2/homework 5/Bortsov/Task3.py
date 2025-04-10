def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)
list = [1, 2, 6, 2, 4, 4, 8, 2, 6]
kick_out(list, 2)
print(list)