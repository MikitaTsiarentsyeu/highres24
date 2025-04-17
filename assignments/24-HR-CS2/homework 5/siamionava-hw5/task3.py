def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)

t = [1, 2, 3, 4, 2, 5, 2, 6]
kick_out(t, 2)
print(t)