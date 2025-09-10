'''Definition: Functions are defined using the def keyword followed by the function
name and parentheses ( ) . They can accept parameters (input) and can return a
value.'''

#Syntax
def function_name(parameters):
    # Function body
    return value

#Calling Function
#function_name(arguments)

#Example
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

#example
def add(a, b):
    return a + b

print(add(2,3))

#example
def discount(cost,d):
    ans=cost-(cost*(d/100))
    print (ans)

discount(100,20)

'''
print() is used to display output to the console.
It's used for debugging or providing information to the user.
It doesn't affect the flow or output of the function itself.


return exits the function and optionally passes back an expression to the caller.
It is used to send the function's result back to where the function was called.
Once return is executed, the function terminates.'''



def greet(name):
    print(f"Hello, {name}!")  # This will print the greeting to the console

def add(a, b):
    return a + b  # This will return the sum to the caller

# Calling the greet function
greet("Alice")
# Output: Hello, Alice!

# Calling the add function
sum_result = add(3, 5)
print(sum_result)  # Output: 8
#---------------------------------------------------------------------
def discount(cost,d):
    ans=cost-(cost*(d/100))
    return ans
x=int(input("Enter Cost:"))
y=int(input("Enter Discount"))
print("The Final Discounted Price is:",discount(x,y))

#--------------------------------------------------------------------
def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini=l[i]
    return mini

def list_max(l):
    maxi=l[0]
    for i in range(len(l)):
        if (l[i]>maxi):
            maxi=l[i]
    return maxi

def list_appendend(l,z):
    newl=[]
    for i in range(len(z)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])
    return newl


def list_appendbefore(l,z):
    newl=[]
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(z)):
        newl.append(l[i])
    return newl

def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    ans = sum / len(l)
    return ans

'''def list_average(l):
    return sum(l) / len(l)  # This will directly compute the average
'''


l=[1,2,3,4,5,-10,6,4]
print("Mini:",list_min(l))
print("Maxi:",list_max(l))
z=[10,20,30]
print(list_appendbefore(l,z))
print(list_appendend(l,z))
print(list_average(z))