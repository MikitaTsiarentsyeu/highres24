def kick_out(l: list, val: object) -> None:
    for i in range(len(l)-1, -1, -1):
        if l[i] == val:
            del l[i]

def get_user_list() -> list:
    while True:
        user_input = input("Enter list elements separated by spaces: ")
        try:
            return [float(x) if '.' in x else int(x) for x in user_input.split()]
        except ValueError:
            return user_input.split()
        
def get_value_to_remove() -> object:
    val = input("Enter value to remove: ")
    try:
        return float(val) if '.' in val else int(val)
    except ValueError:
        return val

if __name__ == "__main__":
    my_list = get_user_list()
    value_to_remove = get_value_to_remove()

    original_list = my_list.copy()

    kick_out(my_list, value_to_remove)

    print(f"\nOriginal list: {original_list}")
    print(f"Value removed: {value_to_remove}")
    print(f"Modified list: {my_list}")

