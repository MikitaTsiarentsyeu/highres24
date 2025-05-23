class Rectangle:
    def __init__(self, length: float, width: float):
        self.__length = None
        self.__width = None
        self.set_dimensions(length, width)

    def set_dimensions(self, length: float, width: float) -> None:
        
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.__length = length
        self.__width = width

    def calculate_area(self) -> float:
       
        return self.__length * self.__width

    def calculate_perimeter(self) -> float:
       
        return 2 * (self.__length + self.__width)

    def get_dimensions(self) -> tuple:
       
        return self.__length, self.__width


if __name__ == "__main__":
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(10, 2.5)

    for i, rect in enumerate([rect1, rect2], start=1):
        length, width = rect.get_dimensions()
        print(f"Rectangle {i} dimensions: Length = {length}, Width = {width}")
        print(f"Area = {rect.calculate_area()}")
        print(f"Perimeter = {rect.calculate_perimeter()}")
        print("---")