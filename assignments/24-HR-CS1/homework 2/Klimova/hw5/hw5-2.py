import math

def is_prime(numb: int) -> bool:
    if numb <= 1:
        return False
    if numb == 2:
        return True
    if numb % 2 == 0:
        return False
    
    max_divisor = math.isqrt(numb) + 1
    for i in range(3, max_divisor, 2):
        if numb % i == 0:
            return False
    return True