class Person: #with and without () # Super class
    def __init__(self, name, age):
        self.name = name
        self.age = age #two underscore after . will lock the info #private member

    def display(self):
        print(self.name, self.age)

