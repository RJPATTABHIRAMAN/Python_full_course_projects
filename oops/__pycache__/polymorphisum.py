from abc import ABC,abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
class Trianlge(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height=height
    def area(self):
        return self.base*self.height*0.5
    

class Square(Shape):
    def __init__(self,width):
        self.width = width
    def area(self):
        return self.width**2
class Pizza(Circle):
    def __init__(self,toping,radius):
        super().__init__(radius)
        self.poping = toping
    
        

shapes= [Circle(5),Square(5),Trianlge(3,4),Pizza("pepper chiken",3)]
for shape in shapes:
    print(shape.area())