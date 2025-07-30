
class Animal:
    def __init__(self,name):
        self.name= name
        self.isAlive = True
    def eat(self):
        print(f"{self.name } is eating")
    def sleep(self):
        print(f"{self.name} is asleep")
class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("moew")
class Mouse(Animal):
    def speak(self):
        print("Squeek")

dog = Dog("gabba")
cat = Cat("rosss")
print(dog.name)      
dog.speak()
print(cat.name)