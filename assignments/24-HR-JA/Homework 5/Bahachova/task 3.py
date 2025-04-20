def kick_out(l, val):
    while val in l:
        l.remove(val)
list = [1, 2, 3, 1, 1, 2, 4, 2, 5, 6]
print("Original list: ", list)
kick_out(list, 1)
print("Changed list: ", list)