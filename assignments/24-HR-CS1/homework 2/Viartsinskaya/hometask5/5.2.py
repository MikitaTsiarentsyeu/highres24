import math

def is_prime(numb: int) -> bool:

    if numb <= 1:
        return False
    if numb <= 3:
        return True
    if numb % 2 == 0 or numb % 3 == 0:
        return False
    
    max_divisor = math.isqrt(numb)
    for i in range(5, max_divisor + 1, 6):
        if numb % i == 0 or numb % (i + 2) == 0:
            return False
        
    return True