def kick_out(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            l.pop(i)
        else:
            i += 1
