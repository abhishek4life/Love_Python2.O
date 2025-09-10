from Person import Person

class Employee(Person):  # Inheriting from Person
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        #super().display()
        #print(self.salary)
        print(self.name, self.age, self.salary)