def test_func(i=0):
    
    print(f"I'm going... {i}")
    test_func(i+1)
    


def fib(n):

    if n <= 1:
        return 1

    return fib(n-2)+fib(n-1)

print(fib(3))



def level1():
    print("level 1 start")
    level2()
    print("level 1 finish")

def level2():
    print("level 2 start")
    level3()
    print("level 2 finish")

def level3():
    print("level 3 start")
    level4()
    print("level 3 finish")

def level4():
    print("level 4 start")
    print("level 4 finish")


# level1()

def level(n, i=0):
    if i == n:
        return

    print((i*"\t")+f"start of level {i+1}")
    level(n, i+1)
    print((i*"\t")+f"finish of level {i+1}")

level(4)
print("the end")

# test_func()


[1,2,3,4,5,6,7,8,9,10]

l = [1,2,3, [4,5,6, [7,8,9]]]

def flatten_sum(l, res=0):

    for i in l:

        if hasattr(i, '__iter__'):
            res = flatten_sum(i, res)
        else:
            res += i

    return res

print(flatten_sum(l))