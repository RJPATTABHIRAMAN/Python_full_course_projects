class Student:
    no_of_Student=0
    class_year = 2026
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.no_of_Student+=1
Student1 = Student("rahul",23)
Student2 = Student("rahul",23)

Student3 = Student("rahul",23)

Student4 = Student("rahul",23)

Student5 = Student("rahul",23)

Student6 = Student("rahul",23)

print(f"My graduvation class of year {Student.class_year} has {Student.no_of_Student} students")
        