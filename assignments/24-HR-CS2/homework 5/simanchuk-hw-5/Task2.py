# Task 2 - Prime number checker
# Wrire a function to check if a number is prime

def is_prime(numb: int) -> bool: 
    if numb < 2:
        return False

    for i in range(2, numb):
        if numb % i == 0:
            return False
        
    return True



print(is_prime(3))
print(is_prime(16))
print(is_prime(2))