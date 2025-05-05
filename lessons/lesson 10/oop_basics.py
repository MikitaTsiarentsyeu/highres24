

class Test: pass

print(type(Test), type(Test()))

class NamedEntity:

    # name = "some name"

    default_name = "default name"

    def __init__(self, name):
        self.name = name
        self.default_val = NamedEntity.default_name

    def print_names(self):
        print(NamedEntity.default_name)
        print(self.name)
    

ne = NamedEntity("test name")
print(ne.name)

ne.print_names()

# ne.new_attr = "new value"
# print(ne.new_attr)

print(ne.__dict__)
print(NamedEntity.__dict__)
print(object.__dict__)


class Dog:

    __colors = ["white", "black", "pink"]

    def __init__(self, name, color, age):
        self.name = name
        self.set_color(color)
        self.set_age(age)

    def bark(self):
        print("woof!")

    # def get_name(self):
    #     return self.__name
    
    # def set_name(self, new_name):
    #     self.__name = new_name

    def set_age(self, new_age):
        if new_age < 0 or new_age > 20:
            raise ValueError("Incorrect age value")
        
        self.__age = new_age

    def get_age(self):
        return self.__age
    
    def __set_color(self, new_color):
        if new_color in Dog.__colors:
            self.__color = new_color
        else:
            self.__color = Dog.__colors[-1]

    def __get_color(self):
        return self.__color
    
    __color = property(__get_color, __set_color)

d = Dog("Zefirka", "white", 4)

print(d.name, d.get_age(), d.color)
# d.age = -100 #error
d.color = "brown"