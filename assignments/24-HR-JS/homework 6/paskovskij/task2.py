import time

def isprime(n: int = 43):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{end_time - start_time:.6f} seconds")
        return result
    return wrapper

timed_isprime = timer(isprime)
print(timed_isprime())