try:
    x = int(input("enter a numeric value:"))
    print("test"+x)
except TypeError:
    print("unsupported operation")
except (ValueError, NameError):
    print("wrong input")
except:
    print("Exception?")


# raise ValueError("boom!")

def div(a:float, b:float) -> float:
    if b == 0:
        raise ValueError(f"argument b should not be a zero")

    return a/b

try:
    x = div(2, 0)
except ValueError:
    try:
        print("wrong function usage")

        x = 2/0
    except ZeroDivisionError:
        print("oooops")
else:
    print("else?")
finally:
    print("runs every time")




