
import time

def operate(l, func):
    for i in l:
        func(i)

l = [1,2,3,4,5]

operate(l, print)

l = ['12', '110', '11']

l = [(1, 3), (3, 0), (2, 1),]

def return_second(x):
    return x[1]

def sum(x, y):
    return x+y

sum = lambda x, y: x+y

print(sorted(l, key=lambda x: x[1]))


# def test_outer():

#     def test_inner():
#         print("inner")

#     return test_inner

# f = test_outer()
# f()

def calculator():

    def add(x, y):
        return x+y
    
    def mult(x, y):
        return x*y
    
    return {'add': add, 'mult': mult}



def logger(level):

    def printer(message):
        print(f"{level}: {message}")

    return printer

pr = logger('ERROR')
pr("test message")



def upper_decor(target_func):

    def wrapper():
        res = target_func()
        return res.upper()
    
    return wrapper

def logging_decor(target_func):

    def wrapper():
        print("start")
        res = target_func()
        print(res)
        print("finish")

    return wrapper

@logging_decor
@upper_decor
def print_test():
    return "test"

# print_test = logging_decor(upper_decor(print_test))
print_test()

