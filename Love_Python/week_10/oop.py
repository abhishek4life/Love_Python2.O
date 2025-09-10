class Student:
    #count = 0   #class variable
    def __init__(self,roll_number,name,total):
        self.roll_number = roll_number
        self.name = name
        self.total = total

    def display(self):
        print(self.roll_number,self.name,self.total)

    def result(self):
        if self.total>=120:
            print("Pass")
        else:
            print("Fail")

s1 = Student(1,"John",100)
#Student.count += 1  #incrementing class variable
s1.display()
s1.result() 

s2 = Student(2,"Jane",150)
#Student.count += 1  #incrementing class variable
s2.display()
s2.result()

# print(Student.count)  #accessing class variable using class name
# print(s1.count)       #accessing class variable using object    name


#Any funtion inside a class is called method
# that's why iniit display result are methods


