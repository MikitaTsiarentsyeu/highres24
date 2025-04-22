def kickOut(list:list, val:object):
    while val in list:
        list.remove(val)
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 5
print(kickOut(list, val))