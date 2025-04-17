def is_prime(numb: int) -> bool:
    if numb < 2:
        return False
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True

t = input("write a number\n")
print(is_prime(int(t)))