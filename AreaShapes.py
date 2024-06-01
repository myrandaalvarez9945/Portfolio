# Here we are going to create an area finder for the given
# values. Of course, it could possibly be better, but for
# now this is an intermediate project, or maybe an easy project
# take it how you see it, but it works.

import math

class Area:
    def __init__(self, width, height, base):
        self.width = width
        self.height = height
        self.base = base

class Square(Area):
    def __init__(self, width):
        super().__init__(width, width, width)
        self.square = width * width

class Rectangle(Area):
    def __init__(self, width, length):
        super().__init__(width, length, width)
        self.rectangle = width * length

class Triangle(Area):
    def __init__(self, base, height):
        super().__init__(base, height, base)
        self.triangle = 0.5 * base * height

class Circle(Area):
    def __init__(self, radius):
        super().__init__(radius, radius, radius)
        self.circle = math.pi * radius ** 2


def main():
    s = Square(5)
    print(s.square)
    r = Rectangle(5,4)
    print(r.rectangle)
    t = Triangle(5,4)
    print(t.triangle)
    c = Circle(3)
    print(c.circle)

if __name__ == "__main__":
    main()