def kick_out(l: list, val: object) -> None:
    i = 0
    while i < len(l):
        if l[i] == val:
            del l[i]
        else:
            i += 1

words = ['apple', 'banana', 'apple', 'cherry', 'apple']
kick_out(words, 'apple')
print(words)
num = [1, 2, 3, 3, 4, 3, 5, 3]
kick_out(num, 3)
print(num)