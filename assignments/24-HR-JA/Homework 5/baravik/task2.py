def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
print(is_prime(17))
print(is_prime(170))