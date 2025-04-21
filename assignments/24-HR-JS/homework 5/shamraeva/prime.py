def is_prime(numb: int) -> bool:
    if numb <= 1:
        return False
    for i in range(2, int(numb ** 0.5) + 1):
        if numb % i == 0:
            return False
    return True
