def is_prime(numb: int) -> bool:
    if numb <= 1:
        return False
    if numb <= 3:
        return True
    if numb % 2 == 0 or numb % 3 == 0:
        return False
    i = 5
    while i * i <= numb:
        if numb % i == 0 or numb % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter a number: "))
print(is_prime(num))