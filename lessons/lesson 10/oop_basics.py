

class Dog:

    __colors = ['white', 'black', 'mixed']

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.set_age(age)

    def __set_color(self, new_color):
        if new_color in Dog.__colors:
            self.__color = new_color
        else:
            raise TypeError("cannot set color")
        
    def __get_color(self):
        return self.__color

    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0 and new_age < 21:
            self.__age = new_age
        else:
            raise TypeError("cannot set age out of bound of 1-20")
        
    color = property(__get_color, __set_color)

    def bark(self):
        print("woof!")

d = Dog("Zefirka", "white", 20)
print(d.color, d.name)

d.bark()

print(d.get_age())

d.color = "black"
print(d.color, d.name)
# d.name = "Max"
# d.color = "black"

# d.breed = "wss"
# print(d.breed)

