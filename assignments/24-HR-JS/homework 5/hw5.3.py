def kick_out(l: list, val: object) -> None:
    x = 0
    while x < len(l):
        if l[x] == val:
            l.pop(x)
        else:
            x += 1

a = [1, 2, 3, 2, 4, 2, 22, 2]
kick_out(a, 2)
print(a)