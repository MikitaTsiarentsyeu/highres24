def IsPrime(numb: int) -> bool:
    if numb < 2:
        return False
    for i in range(2, int(numb ** 0.5) + 1):
        if numb % i == 0:
            return False
    return True

print(IsPrime(1))
print(IsPrime(3))
print(IsPrime(10))
print(IsPrime(11))