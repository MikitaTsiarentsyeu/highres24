def is_prime(x: int) -> bool: 
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True

print(is_prime(2))
print(is_prime(4))