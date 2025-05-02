def prime(numb: int) -> bool:
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True
print(prime(13))
