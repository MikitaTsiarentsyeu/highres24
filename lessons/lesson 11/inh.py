class A:

    def __init__(self, test_atr):
        self.test_atr = test_atr     

    atr_a = "value from A"


    def method_a(self):
        print("method from A")


class B(A):

    def __init__(self, test_atr, new_atr):
        super().__init__(test_atr)
        self.new_atr = new_atr

    atr_a = "VALUIE FROM B"

    def method_a(self):
        print("method from B")

b = B("test value", "new value")
print(b.atr_a)
b.method_a()

print(B.__dict__)
print(A.__dict__)

print(getattr(b, 'atr_a'))