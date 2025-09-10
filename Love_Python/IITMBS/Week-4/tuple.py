print("A tuple is unchangble")

my_tuple = (1, 2, 3)
single_element_tuple = (1,)
print(my_tuple[0])  # Output: 1
print(my_tuple[1:3])  # Output: (2, 3)

#mmutability: Once a tuple is created, you cannot modify its elements. However, you
#can concatenate and create new tuples.
new_tuple = my_tuple + (4, 5)
print(new_tuple)

#nested
nested_tuple = (1, (2, 3), 4)
#unpacking
a, b, c = my_tuple  # a=1, b=2, c=3

#swapping variable
x = 5
y = 10
x, y = y, x  # Now x=10 and y=5 #packing into y and x into tuple then unpacking on lhs x y

#funtion returning tuple
def min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = min_max([1, 2, 3, 4, 5])
print(min_val,max_val)

#count
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # Output: 2

#index
print(my_tuple.index(2))  # Output: 1

'''Use Cases for Tuples
Fixed Data: Use tuples for data that should not change throughout the program.
Dictionary Keys: Tuples can be used as keys in dictionaries because they are immutable.
Multiple Return Values: Use tuples to return multiple values from a function.
'''

import string
print(string.ascii_letters)
#print(string.ascii_uppercase)
s=string.ascii_letters #string
alpha=tuple(s)
print(alpha)

x='abhishek#%$INdiaBharath()bihar patna'
l=list(x)
print(l)

r=[]
for p in l:
    if p  in alpha: #alpha as lookup , dont want to change
        r.append(p)
print(r)

l=list(range(10))
#l._size_()

# When we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple

#
t= 1,3,4 #packing into one
print(t,type(t))

x, y, z =t #unpacking into 3 independent value
print(x,y,z)

p=[10]
print(p,type(p))

y=(10) #single value instead of tuple ,
print(y,type(y))#to make tuple comma , after single value

g=([1,2],[a,b]) #hasable because of list
#g[0]=10 #error
g[0][0]=10
print(g)

'''Hashable means an objeéfkahbe usedaSåkey in a dictionary or an element in a set. To
be hashable:
The object must not change (immutable).
It must have a method to calculate a unique hash value ( __hash__ ).
Examples of hashable objects: Numbers, strings, and tuples. Examples of non-
hashable objects: Lists and dictionaries (because they can change).
Essentially, hashable objects are like permanent ID cards—once created, they can't be
altered, making them reliable for quick lookups in sets and dictionaries. Hope that makes
it clearer! Is there anything else you'd like to know?'''