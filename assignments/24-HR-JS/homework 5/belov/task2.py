def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(170141183460469231731687303715884105727)) #it is))) 