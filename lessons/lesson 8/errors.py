

# print(u_variable)

try:
    a = float(input("enter the value of a:"))
    b = float(input("enter the value of b:"))
    print(a/b)
except ZeroDivisionError:
    print("divided by zero")
    try:
        print(a/b)
    except ZeroDivisionError:
        print("divided by zero again")
except (ValueError, TypeError):
    print("invalid value")
except:
    print("something went wrong")
else:
    print("everything's fine")
finally:
    print("runs every time")


# raise RuntimeError("test raise") 
    

def div(a:float, b:float) -> float:
    if not (isinstance(a, float) and isinstance(b, float)):
        raise RuntimeError("wrong data")

    try:
        return a/b
    except ZeroDivisionError:
        raise RuntimeError("divided by zero")
    except TypeError:
        raise RuntimeError("wrong data")


a = float(input("enter the value of a:"))
b = float(input("enter the value of b:"))
try:
    print(div(a, b))
except RuntimeError as e:
    print(e)
