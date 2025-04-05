import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    test_numbers = [0, 1, 2, 3, 4, 16, 17, 18, 19, 97, 1000003]
    for num in test_numbers:
        print(f"{num} is prime: {is_prime(num)}")