class Rectangle:
    def __init__(self, length, width):
        self.__length = length  
        self.__width = width    

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def get_dimensions(self):
        return f"Length: {self.__length}, Width: {self.__width}"

    def set_dimensions(self, length, width):
        if length > 0 and width > 0:
            self.__length = length
            self.__width = width
        else:
            print("Length and width must be positive numbers.")


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)


print(rect1.get_dimensions())
print(rect2.get_dimensions())

print(f"Area of rect1: {rect1.calculate_area()}")
print(f"Perimeter of rect1: {rect1.calculate_perimeter()}")

rect1.set_dimensions(15, 8)
print(rect1.get_dimensions())
print(f"Updated area of rect1: {rect1.calculate_area()}")

rect2.set_dimensions(-5, 0)
