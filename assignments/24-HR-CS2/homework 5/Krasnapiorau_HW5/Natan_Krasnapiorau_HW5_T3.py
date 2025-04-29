def KickOut(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            l.pop(i)
        else:
            i += 1

list = [1, 2, 3, 3, 4, 5, 3]
KickOut(list, 3)
print(list)