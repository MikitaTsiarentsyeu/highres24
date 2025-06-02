from abc import ABC, abstractmethod

class CarBase(ABC):

    @abstractmethod
    def vroom(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class CarFactory:

    __skus = [('VW', "Passat"), ("Volvo", "VC90")]

    @classmethod
    def add_new_car(parent, make, model):
        if (make, model,) not in parent.__skus:
            parent.__skus.append((make, model,))

    class __SuperCar(CarBase):

        def __init__(self, make, model):
            self.make = make
            self.model = model

        def vroom(self):
            print("vroom!")

        def stop(self):
            print("stopping!")

    @classmethod
    def create_car(parent, make, model) -> CarBase:
        if (make, model,) in parent.__skus:
            return parent.__SuperCar(make, model)
        else:
            raise TypeError("cannot create such a car")
    
    
my_car = CarFactory.create_car("VW", "Passat")
my_car.vroom()

other_car = CarFactory.create_car("Volvo", "VC90")
other_car.vroom()


print(type(CarFactory))

new_class = type("NewClass", (), {"test_attr":"test"})

new_instance = new_class()
print(new_instance.test_attr)

# class NewClass(metaclass=type):

#     test_attr = "test"

class SingletonMeta(type):

    instance = None

    def __call__(self, *args, **kwds):
        if not SingletonMeta.instance:
            SingletonMeta.instance = super().__call__(*args, **kwds)
        
        return SingletonMeta.instance
    
class Logger(metaclass=SingletonMeta):

    pass

l1 = Logger()
l2 = Logger()

print(l1 is l2, id(l1), id(l2))