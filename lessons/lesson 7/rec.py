def test():

    print("to infinity and beyond!")
    test()
    # print("this is a tail")

test()

l = [1,2,3, [4,5,6, [7,8,9]]]

def flatten(l, res=0):
    for i in l:
        if isinstance(i, int):
            res += i
        else:
            res = flatten(i, res)

    return res

print(flatten(l))

def level1():
    print("start of level 1")
    level2()
    print("end of level 1")

def level2():
    print("start of level 1")
    level3()
    print("end of level 1")

def level3():
    print("start of level 1")
    level4()
    print("end of level 1")

def level4():
    print("start of level 1")
    print("end of level 1")

level1()


target = 11

1,2,4,5,6,8,11,134,160