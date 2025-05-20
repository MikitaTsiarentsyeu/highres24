class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def get_dimensions(self):
        return (self.__length, self.__width)

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

# Demonstration
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 2)

print(rect1.get_dimensions())
print(rect1.calculate_area())
print(rect1.calculate_perimeter())