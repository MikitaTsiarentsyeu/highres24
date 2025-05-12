def combinations(lst, r):
    n = len(lst)
    if r > n:
        return
    if r == 0:
        yield []
        return
    if n == 0:
        return

    first = lst[0]
    remaining = lst[1:]
    for combo in combinations(remaining, r - 1):
        yield [first] + combo

    yield from combinations(remaining, r)

my_list = [1, 2, 3]
r_size = 2
print(f"Combinations of size {r_size} from list {my_list}:")
for combo in combinations(my_list, r_size):
    print(combo)
