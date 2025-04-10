def operate(l, f):
    for i in l:
        f(i)

l = [1,2,3,4,5]
operate(l, print)

lambda x, y: x+y

l = ['24', '201', '3' ]

print(sorted(l, key=int))

l = [[1, 0], [2, 3], [4, 2]]

print(sorted(l, key=lambda x: x[1]))

def test():

    def inner():
        print("inner")

    return inner

x = test()
print(x)
x()

# test()()

def calculator():

    def add(x, y):
        return x+y
    
    def multi(x, y):
        return x*y
    
    return {'add': add, 'mult':multi}


def logger(level):

    def print_message(message):
        print(f"{level}: {message}")

    return print_message

error_logger = logger("ERROR")
error_logger("test message")

warning_logger = logger("WARNING")
warning_logger("test message")


def return_upper_str(target_f):

    def wrapper():
        res = target_f()
        return res.upper()
    
    return wrapper

def logging_decor(f):

    def wrapper():
        print("start of func")
        res = f()
        print(res)
        print("end of func")
        return res
    
    return wrapper

@return_upper_str
@logging_decor
def return_test():
    return "test"

# return_test = return_upper_str(return_test)
print(return_test())

import time

start = time.time()

for i in range(1100000):
    i+=1

finish = time.time()

print(finish - start)