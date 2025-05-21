def kick_out(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            del l[i]
        else:
            i += 1
marks = [5, 8, 7, 10, 9, 8, 3, 5, 4]
kick_out(marks, 8)
print(marks) 