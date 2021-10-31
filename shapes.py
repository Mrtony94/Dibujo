class WrongDimensionsError(Exception):
    def __init__(self):
        super().__init__("Wrong dimensions")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Shape:
    ID = 1

    def __init__(self, point=Point(0, 0)):
        self.point = point
        self.id = Shape.ID
        Shape.ID += 1

    def area(self):
        pass

    def __str__(self):  # Devolver una cadena de caracteres con el estado actual del objeto
        return f"{self.__class__.__name__}: {self.point}[{self.id}]"


class Rectangle(Shape):
    def __init__(self, width, height, point=Point(0, 0)):
        super().__init__(point)
        self.width = width
        self.height = height

    def area(self):
        if self.width < 0 or self.height < 0:
            raise WrongDimensionsError()
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side, point=Point(0, 0)):
        super().__init__(side, side, point)


class Ellipse(Shape):
    def __init__(self, a, b, point=Point(0, 0)):
        super().__init__(point)
        self.a = a
        self.b = b

    def area(self):
        import math

        if self.a < 0 or self.b < 0:
            raise WrongDimensionsError()
        return math.pi * self.a * self.b


class Circle(Ellipse):
    def __init__(self, radius, point=Point(0, 0)):
        super().__init__(radius, radius, point)


# p = Point(1, 2)
# s1 = Shape(p)  # id: 1
# print(s1)
# s2 = Shape()  # id: 2
# print(s2)
