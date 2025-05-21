import time
def timer(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    return result, f"{end_time - start_time} seconds"

def Program():
    time.sleep(1)  
    return "A dream, i saw a dream, a dream that wouldn't end over and over again i repeated and corrected every mistake"

print(Program)