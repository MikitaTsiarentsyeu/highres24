def is_prime(numb: int) -> bool:
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True

print(is_prime(13))