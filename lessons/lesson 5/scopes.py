
x = "global"
num = 5

l = []

def test():
    x = "local"
    global num
    num += 2
    print(x)
    new_test = "local"
    l.append(2)

test()
print(x, num, l)


l = [1,2,3,4,5]

def test(l:list):
    l.append(10)

test(l)

print(l)


for i in l:
    i += 1

print(i)

# [xi for xi in range(10)]

# print(xi)