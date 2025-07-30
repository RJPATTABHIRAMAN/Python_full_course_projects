class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    #implmeting method overridig 
    def describe(self):
        print(f"It is {self.color} color {'filled'if self.is_filled  else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
    def describe(self):
         print(f"Area of Circle {3.14*self.radius**2}")
         super().describe()
class Square(Shape):
    def __init__(self, color, is_filled,width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
         super().describe()
         print(f"Area of sqare {self.width*self.width}")
class Triangle(Shape):
    def __init__(self, color, is_filled,width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"Area of Triangle {0.5*self.width*self.height}")
        super().describe()

circle = Circle(color="red",is_filled=True,radius=5)
print(circle.radius)
sqaure = Square(color="blue",is_filled=False,width=4)
print(sqaure.color)
circle.describe()
sqaure.describe()