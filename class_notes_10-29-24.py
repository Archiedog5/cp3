import math
from abc import ABC, abstractmethod 
#polymorphism functions or mehtods can do multipule hings based on given inputs.

class Shape(ABC):
    def __init__(self,x):
        self.x=x

    def area(self):
        return 0
class Square(Shape):
    def area(self):
        return self.x * self.x

class Circle(Shape):
    def area(self):
        return round(math.pi*self.x**2,2)
class Rectangle(Shape):
    def __init__(self, x,y):
        super().__init__(x)
        self.y = y
    def area(self):
        return self.x*self.y
    
shapes = [Square(4),Circle(4),Rectangle(5,3),Shape(6), "this"]
for shape in shapes:
    if isinstance(shape, Shape):
        print(shape.area())