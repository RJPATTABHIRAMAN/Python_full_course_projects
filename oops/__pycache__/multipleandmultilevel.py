class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is Eating")
    def sleep(self):
        print(f"This {self.name} is sleeping")
class Pray(Animal):
    def flee(self):
        print(f"This {self.name} is feeling")
class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")
class Rabit(Pray):
    pass
class Hawk(Predator,Pray):
    pass
rabit = Rabit("robooow")
hawk = Hawk("kichch")
hawk.hunt()
hawk.flee()
rabit.flee()

