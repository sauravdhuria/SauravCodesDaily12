from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(self.side **2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(self.length * self.breadth)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(self.radius **2)

r1 = Square(45)
r1.area()
r2= Rectangle(5,5)
r2.area()
r3=Circle(5)
