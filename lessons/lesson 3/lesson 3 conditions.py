x = False

if x > 0:
    print("it's positive")
elif x == 0:
    print("it's zero")
    if isinstance(x, bool):
        print("it's False")
else:
    print("it's negative")

print("the end")

x = "test" if True else "not test"