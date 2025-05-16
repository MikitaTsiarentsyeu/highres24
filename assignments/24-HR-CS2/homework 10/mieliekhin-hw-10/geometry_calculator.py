import numbers

class Rectangle:
    __length: float
    __width: float
    
    def __init__(self, length: float, width: float):
        if not isinstance(length, numbers.Number) or not isinstance(width, numbers.Number):
            raise TypeError("sides must be numbers")
        
        if length <= 0 or width <= 0:
            raise ValueError("sides must be positive numbers")

        self.__length = length
        self.__width = width
    
    def calculate_area(self):
        return self.__length * self.__width
    
    def calculate_perimeter(self):
        return 2 * self.__length + 2 * self.__width
    
    def get_dimensions(self):
        return f"Length: {self.__length}, width: {self.__width}"

    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width
    
    length = property(get_length)
    width = property(get_width)
    
rectangle1 = Rectangle(12.343434, 34.343434)
print(rectangle1.get_dimensions())
print(rectangle1.get_length())
print(rectangle1.get_width())
print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())

rectangle2 = Rectangle(1, 1)
print(rectangle2.get_dimensions())
print(rectangle2.get_length())
print(rectangle2.get_width())
print(rectangle2.calculate_area())
print(rectangle2.calculate_perimeter())

            
