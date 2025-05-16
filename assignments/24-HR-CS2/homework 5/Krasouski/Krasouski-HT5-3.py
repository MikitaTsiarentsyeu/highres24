import random

def kick_out(l: list, val: object) -> None:
    i = 0
    endValue = 0

    while i < len(l) - endValue:
        if l[i] == val:
            l[i], l[len(l) - 1 - endValue] = l[len(l) - 1 - endValue], l[i]
            endValue += 1
        else:
            i += 1

    del l[len(l) - endValue:]

l = [random.randint(0, 15) for _ in range(100)]
print (l)

kick_out(l, 3)
print(l)