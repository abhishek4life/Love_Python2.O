# class Student:
#
#     def __init__(self, roll_no, name, marks):
#         self.roll_no = roll_no
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print(self.roll_no, self.name, self.marks)
#
#
# class Employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
#     def display(self):
#         print(self.name,self.age,self.salary)
#
# s = Student(0, 'Bhuvnesh', 150)
# s.display()
#
# e = Employee('Harsh',30,50000)
# e.display()

#name,age are common in both

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Person: #with and without () # Super class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):  # Inheriting from Person
    def __init__(self, name, age, marks):
        super().__init__(name, age) #
        self.marks = marks

    def display(self):    #super().display()
        #super().display()
        print(self.name, self.age, self.marks)


class Employee(Person):  # Inheriting from Person
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        #super().display()
        #print(self.salary)
        print(self.name, self.age, self.salary)


# Test cases
p = Person("Ravi", 25)
p.display()

s = Student("Amit", 20, 85)
s.display()

e = Employee("Neha", 30, 50000)
e.display()
