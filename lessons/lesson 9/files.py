import os

print(os.getcwd())

with open("test.txt", 'w') as f:

    f.write("new content\n")

with open("test.txt", 'a') as f:

    f.write("appended content\n")
    

with open("test.txt", 'r') as f:

    # print(f.readlines())
    for line in f:
        print(line)

with open("test.txt", 'w+') as f:

    f.write("new content\n")
    f.seek(0)
    f.write("vvvvv")
    print(repr(f.read()))

with open("test.txt", 'a+') as f:

    f.write("append content\n")
    f.seek(0)
    f.write("ccccc")
    print(repr(f.read()))

with open("test.txt", 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write("test r+")