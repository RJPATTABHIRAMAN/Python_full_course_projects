
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name} , {self.position}"
    @staticmethod
    def is_valid_postion(position):
        valid_position = ["manager","Engineer", "Cook"]
        return position in  valid_position
print(Employee.is_valid_postion("Cook")
        )
Employee1 = Employee("RAHUL","MANEGER")
print(Employee1.name)