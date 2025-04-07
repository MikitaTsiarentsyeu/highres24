
print(sum([1,2,3,4,5]))

def sum(a, b):
    return a+b

print(sum(3, 2))
print(sum('3', '2'))

# def sum(a, b, c):
#     return sum(sum(a, b), c)

# sum(2, 3, 4)

def exec(a=0, b=0, c=0):
    return a+b*c

print(exec(b=2, c=3))

# print(1,2,3,4,5,6,7,8,9,10)

def sum(*args):
    print(args, type(args))

sum(1,2,3,4,5,6,7,8,9,10)

l = [1,2,3,4,5]
sum(*l)

def test(**kwargs):
    print(kwargs, type(kwargs))

test(test=1, first="test")

def test(x):

    if x == 0:
        return "zero"
    if x > 0:
        return True
    else:
        return False

res = test(10)
print(res, type(res))

def test():
    return 5, "test", True

res = test()
print(res, type(res))

a, b, c = test()
print(a, b, c)

print