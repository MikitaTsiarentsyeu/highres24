# for i in range(10):
#     print(i)

# print(list(range(10000000000)))

def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
    
for i in my_range(10):
    print(i)

def test():
    yield 1
    yield 2
    yield 3
    yield from test()

for i in test():
    print(i)