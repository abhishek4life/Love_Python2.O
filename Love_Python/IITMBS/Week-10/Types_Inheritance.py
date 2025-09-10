'''
Simple inheritance->One Parent-->One Child
Hierarchical inheritance = One Parent --> Three Child
Multiple inheritance = TWo PArent--> One child
Multilevel inheritance = Parent class---> Intermediate class----> Child Class
Hybrid Inheritance = ANy combination above

'''


'''**Types of Inheritance in Python**

In Python, inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another class. Here are the five main types of inheritance:

### **1. Single Inheritance**

- **Definition**: A derived class inherits from only one base class. This is the simplest form of inheritance where a child class inherits from a single parent class.
- **Example**: A `Dog` class inheriting from an `Animal` class.

### **2. Multiple Inheritance**

- **Definition**: A derived class inherits from two or more base classes. This allows a class to combine features from multiple parent classes.
- **Example**: A `Duck` class inheriting from both `Flyer` and `Swimmer` classes.

### **3. Multilevel Inheritance**

- **Definition**: A derived class inherits from another derived class, creating a chain of inheritance. This type of inheritance allows for a hierarchical structure where a class inherits from a class that itself inherits from another class.
- **Example**: A `GrandChild` class inheriting from a `Child` class, which in turn inherits from a `Parent` class.

### **4. Hierarchical Inheritance**

- **Definition**: Multiple derived classes inherit from a single base class. This type of inheritance is useful when several classes share common features from a single parent class.
- **Example**: Classes like `Dog`, `Cat`, and `Horse` all inheriting from an `Animal` class.

### **5. Hybrid Inheritance**

- **Definition**: A combination of two or more types of inheritance. This allows for complex relationships between classes, combining features from different inheritance types.
- **Example**: A `Student` class inheriting from both `Employee` (which inherits from `Person`) and `Athlete` classes, showcasing a mix of hierarchical and multiple inheritance.

**Key Points:**

- **Single Inheritance** is straightforward and promotes code reusability.
- **Multiple Inheritance** can lead to the "Diamond Problem" where ambiguity arises in method resolution. Python uses Method Resolution Order (MRO) to resolve this.
- **Multilevel Inheritance** allows for extended functionality and attribute sharing across generations of classes.
- **Hierarchical Inheritance** is useful for creating classes with common sets of methods and properties.
- **Hybrid Inheritance** provides flexibility in modeling complex relationships but can increase complexity in code maintenance.

**Syntax and Usage:**

- **Single Inheritance**: 
  ```python
  class Parent:
      pass
  class Child(Parent):
      pass
  ```

- **Multiple Inheritance**: 
  ```python
  class Parent1:
      pass
  class Parent2:
      pass
  class Child(Parent1, Parent2):
      pass
  ```

- **Multilevel Inheritance**: 
  ```python
  class GrandParent:
      pass
  class Parent(GrandParent):
      pass
  class Child(Parent):
      pass
  ```

- **Hierarchical Inheritance**: 
  ```python
  class Parent:
      pass
  class Child1(Parent):
      pass
  class Child2(Parent):
      pass
  ```

- **Hybrid Inheritance**: 
  ```python
  class Parent1:
      pass
  class Parent2:
      pass
  class Child1(Parent1):
      pass
  class Child2(Parent1, Parent2):
      pass
  ```

**Conclusion:**

Inheritance in Python provides a powerful mechanism for code reuse, organization, and modeling real-world relationships. Each type of inheritance serves different purposes, from simple code reuse to complex class hierarchies. Understanding these types helps in designing efficient, maintainable, and extensible software systems.

'''