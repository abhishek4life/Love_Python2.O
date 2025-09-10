#TYpe of Function argument
#keyword Argument
def add(c,a,b):
    return(a+b-c)
print(add(a=20,b=30,c=40))

#default argument
def add(c,a=20,b=30):
    return(a+b-c)
print(add(40))
print(add(40,10))
print(add(40,10,50))
print(add(40,b=10,a=50))

#---------------------------------------------------------

def add(c,a=20,b=30):
    print(a+b-c) #printing 10,0,20

print(add(40))  # Calls add(40, 20, 30) -> prints 10 and returns None
print(add(40, 10))  # Calls add(40, 10, 30) -> prints 0 and returns None
print(add(40, 10, 50))  # Calls add(40, 10, 50) -> prints 20 and returns None
print(add(40, b=10, a=50))  # Calls add(40, 50, 10) -> prints 20 and returns None

#why getting None?
'''The None you're seeing in the output is because the add function doesn't explicitly
return a value. By default, if a function doesn't have a return statement, it returns None .'''

#----------------------------------------------------------------------------------------------------------------------
#Type of Function

#inbuilt function
# print(),input(),len()

#library function
 #log(),sqrt(),random(),randrange(),calendar(),month()
 #math.log(),random.random(),calender.month()

#string method (funtion)
 #upper(),lower(),strip(),count(),index(),replace()
 #.upper(),.lower()

#User defined Function
'''def square(x):
    sqr=x**2
    return sqr
print(square(5))'''

