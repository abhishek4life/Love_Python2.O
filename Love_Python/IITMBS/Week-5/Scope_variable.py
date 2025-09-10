def myfunction(x):
    x = x * 2
    print("Value of x in function call:", x)  # 10 #wrong

x = 5
print("Value of x before function call:", x)  # 5 #wrong
myfunction(x)
print("Value of x after function call:", x)  # 10 #wrong

#--------------------------------------------------------
'''Variable Scope in Python
In Python, variable scope refers to where in your code a variable can be accessed. There are mainly two types of scope:

1. Local Scope
Variables created inside a function have local scope.
They can only be used inside that function.'''

def greet():
    name = "Alice"  # Local variable
    print(f"Hello, {name}!")

greet()  # Outputs: Hello, Alice!
#print(name)  # This will cause an error because 'name' is not accessible here

'''2. Global Scope
Variables created outside of functions have global scope.
They can be accessed from anywhere in the code.'''

message = "Welcome!"  # Global variable

def greet():
    print(message)

greet()  # Outputs: Welcome!
print(message)  # Also outputs: Welcome!

#Important Points to Remember

'''Accessing Global Variables:
You can access global variables inside functions.
But to modify a global variable inside a function, you need to use the global keyword.'''
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Outputs: 1

'''Variable Shadowing:
If you create a local variable with the same name as a global variable, 
it will shadow (hide) the global variable within that function.'''

x = 10

def print_x():
    x = 20  # This creates a new local variable, doesn't affect the global x
    print(x)

print_x()  # Outputs: 20
print(x)   # Outputs: 10 (global x is unchanged)

'''Nested Functions:
Functions inside functions create nested scopes.
Inner functions can access variables from outer functions'''

def outer():
    x = "outer"
    def inner():
        print(x)  # Can access x from the outer function
    inner()

outer()  # Outputs: outer

