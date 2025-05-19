def kick_out(l: list, val: object) -> None:
    if not isinstance(l, list):
        raise TypeError("First argument must be a list")
    
    # Iterate backwards to avoid index shifting issues
    for i in range(len(l) - 1, -1, -1):
        if l[i] == val:
            del l[i]
