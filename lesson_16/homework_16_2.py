from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def area(self):
        """Площадь фигуры"""
        pass

    @abstractmethod
    def perimeter(self):
        """Периметр фигуры"""
        pass

    def __str__(self):
        return self.__class__.__name__


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("width и height должны быть > 0")
        self.__width = float(width)
        self.__height = float(height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("radius должен быть > 0")
        self.__radius = float(radius)

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return pi * self.__radius ** 2

    def perimeter(self):
        return 2 * pi * self.__radius


class Triangle(Figure):
    def __init__(self, a, b, c):
        for name, val in (("a", a), ("b", b), ("c", c)):
            if val <= 0:
                raise ValueError(f"сторона {name} должна быть > 0")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("такой треугольник не существует")
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    @property
    def sides(self):
        return self.__a, self.__b, self.__c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5


if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Triangle(3, 4, 5),
    ]

    for sh in shapes:
        print(f"{sh}: S={sh.area():.3f}, P={sh.perimeter():.3f}")
