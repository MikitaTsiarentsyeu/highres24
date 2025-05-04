import os

print(os.getcwd())

with open('test.txt', 'w+') as f:
    print(f, type(f))

    f.write("test text\n")

with open('test.txt', 'a+') as f:
    f.write("appended text\n")

with open('test.txt', 'r+') as f:
    print(repr(f.readlines()))

# f.close()

with open('test.txt', 'a+') as f:
    print(repr(f.read()))
    f.seek(0)
    f.write("TEST")


with open('test.txt', 'r+') as f:
    print(repr(f.read()))
    f.seek(0)
    f.write("TEST")