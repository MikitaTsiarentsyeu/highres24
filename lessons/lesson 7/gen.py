

print(list(range(100)))

for i in range(10):
    print(i)



def test():
    print("first")
    yield 0
    print("second")

res = test()
for i in res:
    pass

def my_range(n):
    i = 0
    while True:
        if i == n:
            return
        yield i
        i += 1

for i in my_range(10):
    print(i)

