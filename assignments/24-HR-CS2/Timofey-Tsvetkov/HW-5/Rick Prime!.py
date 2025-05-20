def is_prime(numb: int) -> bool:
    """Check if a number is prime."""
    if not isinstance(numb, int) or numb <= 1:
        return False
    
    if numb == 2:
        return True
    if numb % 2 == 0:
        return False
    
    for i in range(3, int(numb**0.5) + 1, 2):
        if numb % i == 0:
            return False
    return True