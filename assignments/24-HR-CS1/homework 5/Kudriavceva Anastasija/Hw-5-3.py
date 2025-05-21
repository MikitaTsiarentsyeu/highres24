def kick_out(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            del l[i]
        else:
            i += 1
marks = [1, 8, 7, 8, 10, 3, 5, 4]
kick_out(marks, 8)
print(marks) 