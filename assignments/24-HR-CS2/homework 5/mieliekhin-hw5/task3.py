l = [1, 2434, 432, 4, 4, 4, 4]

def kick(l: list, val: object):
    i = 0
    while i < len(l):
        if l[i] == val:
            del l[i]
        else:
            i += 1

kick(l, 4)
print(l)