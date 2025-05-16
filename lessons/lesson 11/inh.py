from abc import ABC, abstractmethod

class Test_Parent:

    test_atr = "test value"

    def test_method(self):
        print("test method")


class Test_Child(Test_Parent): pass

tc = Test_Child()

print(tc.test_atr)
tc.test_method()

Test_Child.test_atr = "child test value"

print(Test_Child.__dict__)
print(Test_Parent.__dict__)


class Dog(ABC):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @abstractmethod
    def woof(self):
        print("bark!")


class HuntingDog(Dog):

    def hunt(self, target):
        print(f"got the {target}")

    def woof(self):
        return super().woof()

class SmartDog(Dog):

    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def woof(self):
        for i in range(self.age):
            super().woof()

    # def woof(self):
    #     print(self.age*"bark!")

sd = SmartDog("Bobby", "poodl", 5)
sd.woof()

hd = HuntingDog("Bobby", "poodl")