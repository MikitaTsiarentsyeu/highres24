def kick_out(l: list, val: object) -> None:
    while val in l:
        l.remove(val)
