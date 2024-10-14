from abc import ABC, abstractmethod
import math

# abstract method "Figure"
class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

# Rectangle class
class Rectangle(Figure):
    def __init__(self, width, height):
        # initialize private attributes for width and height
        self.__width = width
        self.__height = height

    def get_area(self):
        # calculate area of the rectangle
        return self.__width * self.__height

    def get_perimeter(self):
        # calculate perimeter of the rectangle
        return 2 * (self.__width + self.__height)

# Circle class
class Circle(Figure):

    def __init__(self, radius):
        # initialize private attributes for radius
        self.__radius = radius

    def get_area(self):
        # calculate area of the circle
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        # calculate area of the circle
        return 2 * math.pi * self.__radius

    # Triangle class
class Triangle(Figure):
    def __init__(self, a, b, c):
        # initialize private attributes for triangle sides
        self.__a = a
        self.__b = b
        self.__c = c

    def get_area(self):
        # calculate area of the triangle
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def get_perimeter(self):
        # calculate perimeter of the triangle
        return self.__a + self.__b + self.__c

# list of figuresf
figures = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(3, 4, 5)
]

for figure in figures:
    print(f"Figure: {figure.__class__.__name__}")
    print(f"Area: {figure.get_area()}")
    print(f"Perimeter: {figure.get_perimeter()}")
    print("-" * 30)
