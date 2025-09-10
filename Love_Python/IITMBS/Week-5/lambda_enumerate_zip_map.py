#Functional Programming

#lambda Function
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))

#-----------------------------------
add=lambda x,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
div=lambda x,y:x/y

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))
print(type(add)) #class Function

#-------------------------------------

#Enumerate
fruits=["mango","apple","orange","pineapple","watermelon","guava","kiwi"]
size = [5,5,6,6,9,10,5,4]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i,fruits[i])

for fruit in enumerate(fruits):
    print(fruit) #tuple

#----------------------------------------------------------------------------------------

#zip
fruits=["mango","apple","orange","pineapple","watermelon","guava","kiwi"]
size = [5,5,6,6,9,10,5,4]
print(zip(fruits,size)) #zip object
print(list(zip(fruits,size))) #list of tuple
print(dict(zip(fruits,size)))

#-------------------------------------------------------------------------------------------
#Map

a=[10,20,30,40,50,60]
b=[5,10,15,20,25,30]
#c=a-b #unsupported operand type(s) for -: 'list' and 'list'
##c=a[0]-b[0] #works
#print(c)

def sub(x,y):
    return x-y

def incr(x):
    return x+1

c=map(sub, a,b)
print("List C:",list(c))
c=map(incr,a)
print("List C:",list(c))

#-------------------------------------------
#filter
import math
a=[25,-16,9,81,-100]
def square_root(n):
    return math.sqrt(n)
#c=map(square_root,a) #error bcz of -16

#For Filter
def is_positive(n):
    if n>=0:
        return n

c=map(square_root,filter(is_positive,a)) #For Filter
print(list(c))