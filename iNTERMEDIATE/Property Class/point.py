class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise ValueError("X coordinate is read-only!")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        return ValueError("Y coordinate is read-only!")


point = Point(12, 5)
print(point.x)
print(point.y)

point.x = 100



import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


circle = Circle(30)
circle.radius
circle.diameter

circle.diameter = 100
circle.diameter
circle.radius
