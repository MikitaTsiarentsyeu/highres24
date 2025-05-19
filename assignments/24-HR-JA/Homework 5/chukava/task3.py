def remove_all(lst: list, value) -> None:
    i = 0
    while i < len(lst):
        if lst[i] == value:
            lst.pop(i)
        else:
            i += 1