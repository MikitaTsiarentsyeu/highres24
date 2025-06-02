class Parent:

    def test_method(self):
        print("Parent")

class Child:

    def test_method(self):
        print("Child")

p = Parent()
c = Child()

# p.test_method()
# c.test_method()

def call_test_method(instance: Parent):
    instance.test_method()

# for i in [p, c]:
#     call_test_method(i)


print(2 + 3)
print('2' + '3')

print(int(2).__add__(3))
print('2'.__add__('3'))


class FreightTrain:

    def __init__(self, cart_count):
        self.cart_count = cart_count

    def __str__(self):
        return f"{FreightTrain.__name__}({self.cart_count})"
    
    def __eq__(self, other):
        
        try:
            if self.cart_count == other.cart_count:
                return True
        except AttributeError:
            return False

        
        return False
    
    def __add__(self, other):
        try:
            return FreightTrain(self.cart_count + other.cart_count)
        except AttributeError:
            raise TypeError("cannot add non-FreightTrain object")
    
ft = FreightTrain(5)
print(ft)

print(ft == ft)
print(ft == FreightTrain(5))
print(ft == FreightTrain(10))
print(ft == 5)

print(ft + FreightTrain(10))
# print(5 + ft)
# int(5).__add__(ft)

print(ft + 5)
ft.__add__(5)