from Person import Person

class Student(Person):  # Inheriting from Person
    def __init__(self, name, age, marks):
        super().__init__(name, age) #
        self.marks = marks

    def display(self):    #super().display()
        #super().display()
        print(self.name, self.age, self.marks)
