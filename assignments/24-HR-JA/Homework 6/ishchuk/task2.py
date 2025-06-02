import time

def measure_time(function):
    def wrapped_function(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(function.__name__, "completed in", round(duration, 4), "seconds")
        return result
    return wrapped_function

@measure_time
def do_fast():
    total = sum(range(1000))
    return total

@measure_time
def do_slow():
    time.sleep(1)

@measure_time
def do_medium():
    count = 0
    for _ in range(1000000):
        count += 1
    return count

do_fast()
do_slow()
do_medium()
