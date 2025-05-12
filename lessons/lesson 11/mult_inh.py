class A:

    def target_method(self):
        print("class A!")

class B:

    def target_method(self):
        print("class B!")

class C:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def target_method(self):
        self.a.target_method()
        self.b.target_method()

c = C(A(), B())
c.target_method()

print(C.mro())

