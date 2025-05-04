def kick_out(l, val):
    i = 0
    while i < len(l):
        if l[i] == val:
            l.pop(i) 
        else:
            i += 1 

marks = [10, 9, 10, 8, 7, 4, 4, 4, 3, 5, 4]

kick_out(marks, 4)

print(marks)
