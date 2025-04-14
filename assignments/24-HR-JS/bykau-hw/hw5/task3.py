def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)

l = list(map(int, input("List: ").split(',')))
val = int(input("Value to remove: "))
kick_out(l, val)
print(l)
