
class Zero:

    def test_method(self):
        print(Zero.__name__)

class A(Zero):

    def test_method(self):
        print(A.__name__)

    def __str__(self):
        return A.__name__

class B(Zero):

    def test_method(self):
        print(B.__name__)

    def __str__(self):
        return B.__name__

class C(A, B):

    def test_method(self):
        return super().test_method()

c = C()
c.test_method()
# print(c)

print(C.mro())