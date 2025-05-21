
class Parent:

    def test_method(self):
        print("parent")

class Child(Parent):
    
    def test_method(self):
        print("child")

p = Parent()
c = Child()

p.test_method()
c.test_method()

def Test_Method_Call(obj: Parent):
    obj.test_method()


for i in [p, c, object, "test"]:
    try:
        Test_Method_Call(i)
    except AttributeError:
        print("the object does not implement .test_method()")


def test_add(a, b):
    return a+b

print(test_add(2, 3))
print(test_add('2', '3'))

print('2'.__add__('3'))

print(dir(str))
print(dir(int))


class FreightTrain:

    def __init__(self, cart_count):
        self.cart_count = cart_count

    def __str__(self):
        return f"{FreightTrain.__name__}({self.cart_count})"
    
    def __int__(self):
        return self.cart_count
    
    def __eq__(self, other):
        if id(self) == id(other):
            return True
        
        # if str(self) == str(other):
        #     return True

        try:
            if self.cart_count == other.cart_count:
                return True
        except AttributeError:
            return False
        
        return False
    
    def __len__(self):
        return self.cart_count
    

f = FreightTrain(2)
print(f, int(f))


new_f = FreightTrain(10)
print(f == new_f)
print(f == FreightTrain(2))
print(f == 2)
print(len(f))