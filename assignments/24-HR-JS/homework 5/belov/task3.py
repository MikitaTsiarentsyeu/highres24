def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 3, 3,3, 3, 3, 3, 3, 3]
kick_out(list, 3)
print(list)