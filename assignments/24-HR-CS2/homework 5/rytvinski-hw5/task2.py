def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

print(is_prime(3))
print(is_prime(9))
print(is_prime(8))
print(is_prime(7))