def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)
        
    
l = [1, 2, 3, 4, 5, 6, 7]
kick_out(l, 3)
print(l)