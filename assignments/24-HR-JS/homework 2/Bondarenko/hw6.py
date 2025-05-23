def operate(l, f):
    for i in l:
        f(i)

l = [1, 2, 3, 4, 5]
operate(l, print)

def add(x, y):
    return x + y

print(add(3, 5))

l = ['24', '201', '3']
numbers = []
for s in l:
    numbers.append(int(s))
sorted_numbers = sorted(numbers)
sorted_strings = []
for num in sorted_numbers:
    sorted_strings.append(str(num))
print(sorted_strings)

l = [[1, 0], [2, 3], [4, 2]]
for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j][1] > l[j + 1][1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)

def test():
    def inner():
        print("inner")
    return inner

x = test()
print(x)
x()
test()()

def calculator():
    def add(x, y):
        return x + y
    def multi(x, y):
        return x * y
    return {'add': add, 'mult': multi}

calc = calculator()
result1 = calc['add'](3, 5)
result2 = calc['mult'](3, 5)
print(result1)
print(result2)

def logger(level):
    def print_message(message):
        print(level + ": " + message)
    return print_message

error_logger = logger("ERROR")
error_logger("test message")
warning_logger = logger("WARNING")
warning_logger("test message")

def return_test():
    return "test"

print("start of func")
result = return_test()
result = result.upper()
print(result)
print("end of func")

import time
start = time.time()
for i in range(1100000):
    i = i + 1
finish = time.time()
print(finish - start)