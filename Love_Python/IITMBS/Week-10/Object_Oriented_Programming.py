
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Class and Object

'''Class: A class is like a blueprint or template that defines the structure and behavior (properties and methods) of
 objects. It outlines the data (attributes) and functionalities (methods) that the objects created from the 
 class will have.'''

'''Object: An object is an instance of a class. It represents a specific entity created using the class blueprint.
 Objects hold actual data and can perform the behavior defined in the class.'''


Creating Class
class Student:
    roll_no = None
    name = None

s0 = Student() #Special Type of Fn #constructor
s0.roll_no = 0
s0.name = 'Bhuvnesh'
print(s0.roll_no,s0.name)

# s1 = Student()
# print(s1.roll_no,s1.name)
#
# s2 = Student()
# s2.roll_no = 2
# s2.name = 'HArish'
# print(s2.roll_no,s2.name)
#
# s50 = Student()
# s50.name = 'Asmita'
# print(s50.roll_no,s50.name)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #Attributes and Methods
#
# class Student:
#     #variable inside class
#     #count = 0 #class Attribute
#     def __init__(self,roll_no,name,total):
#         # variable in init
#         self.roll_no = roll_no #object attribute
#         self.name = name
#         self.total = total
#
#     def display(self):
#         print(self.roll_no,self.name, self.total)
#
#     def result(self):
#         if self.total > 120:
#             print('Pass')
#         else:
#             print('Fail')
#
#
# s0 = Student(0,'Bhuvnesh', 150) #self=s0
# #Student.count +=1
# s0.display()
# s0.result()
#
# s1 = Student(1,'Harish', 100)#self=s1
# #Student.count +=1
# s1.display()
# s1.result()
#
# #print(Student.count)

'''In object-oriented programming (OOP), **attributes** are fundamental components that define the characteristics 
or properties of an object or class. Here's a detailed overview:

- **Definition**: An attribute is a data member or property associated with an object or class, representing its state
 or characteristics. Attributes can be of various data types, such as integers, strings, Booleans, or even other 
 objects[1][2][3].

- **Types of Attributes**:

  - **Instance Attributes**: These are unique to each instance of a class. They are defined within the constructor of a
   class and are accessible only through the object they belong to. For example, in a `Car` class, each car object might 
   have its own `manufacturer` attribute[1][4].
   
  - **Class Attributes**: These are shared across all instances of a class. They are defined directly in the class body
   and are not unique to any particular instance. An example could be an interest rate for all bank accounts in a 
   `BankAccount` class[4].
   
  - **Simple Attributes**: These are atomic and cannot be further subdivided. For instance, the age of a person[2].
  
  - **Composite Attributes**: These can be broken down into simpler components. An address, which includes street name,
   city, ZIP code, etc., is an example[2].
   
  - **Single-valued Attributes**: These hold a single value for each entity instance, like date of birth[2].
  
  - **Multivalued Attributes**: These can store multiple values, such as email addresses or phone numbers for a person[2].
  
  - **Derived Attributes**: These are calculated or derived from other attributes, like age from date of birth[2].
  
  - **Key Attributes**: These uniquely identify an entity, like a social security number[2].
  
  - **Complex Attributes**: These combine multivalued and composite attributes, rarely used in database management systems[2].

  - **Access and Modification**: Attributes can have different access rights, like private or public. For example, a `Car` 
  class might have a private `manufacturer` attribute, accessible only by instances of the `Car` class[1].

  - **Usage in Programming**: In Python, attributes are accessed using dot notation. For instance, `my_car.manufacturer` 
  would access the `manufacturer` attribute of a `Car` object[5].

  - **Contrast with Methods**: While attributes store data, methods are functions that operate on this data or perform 
  object-specific computations. Methods can change the state of an object by modifying its attributes[4][5].

  - **Importance in OOP**: Attributes and methods together allow objects to model real-world entities effectively, 
  making software development more modular, reusable, and maintainable[5][6].

This comprehensive understanding of attributes in OOP highlights their role in defining the state and behavior of objects, 
crucial for creating robust and maintainable software systems.

'''

