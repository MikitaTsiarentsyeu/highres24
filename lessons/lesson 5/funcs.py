
print(sum([1,2,3,4,5]))

def sum(a, b):
    return a+b

print(sum(2, 3))
print(sum('2', '3'))


def test():
    pass



def exec(a=1, b=2, c=3):
    return a+b*c

print(exec(-5, c=100))


print(1,2,3,4,5,6)

def sum(l):
    res = 0
    for i in l:
        res += i
    return res

def sum(x, y, *args):
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5))

def test(x, y, *args, **kwargs):
    print(x, y)
    print(args)
    print(kwargs)

test(1,2,3,4,5, first=10, second="test", thrird=False)

print(1,2,3,4, sep=',', end='.\n')

def test(x):
    return 2,3,4,5,"test"

    if x:
        return True
    else:
        return False
    print("after the retrun")

res = test(10)
print(res, type(res))