#Comparing Lists and Sets:
from numpy.ma.core import append

#Feature         List                                               Set                                      Tuple
#Order           Ordered                                            Unordered                                ordered
#Duplicates      Allows duplicates                                  No duplicates                            Allow
#Indexing        Supports indexing                                  No indexing                              support
#Mutability      Mutable                                            Mutable_                                 immutable
#Use Case        Ideal for ordered collections                      Ideal for unique elements
#Membership      Less efficient for membership tests                More efficient for membership tests

y={1,2,3,4,5,1}
print(type(y)) #set

import sys
l=list(range(100)) #slow search #Car
s=set(range(100)) #fast search #Bus # object is not subcriptable s[]
print(sys.getsizeof(l))
print(sys.getsizeof(s))



'''Basic Features
Unordered: Sets do not maintain any specific order of elements.
Unique Elements: Each element in a set must be unique. If a duplicate is added, it is
ignored.
Mutable: Sets are mutable, meaning you can add or remove elements after the set is
created.
No Indexing: Because sets are unordered, they do not support indexing, slicing, or
other sequence-like behavior.'''

fruits=set()
# Adding an element
fruits.add('orange')
print(fruits)

# Removing an element
#fruits.remove('banana')  # Raises KeyError if the element is not found
fruits.discard('banana')  # Does not raise an error if the element is not found
print(fruits)

#Set Operation
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1 & set2)  # Output: {3, 4}

# Difference
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Output: {1, 2, 5, 6}

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Subset
print(set1.issubset(set2))  # Output: True

# Superset
print(set2.issuperset(set1))  # Output: True

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))  # Output: True

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
set1.union(set2)  # set1 becomes {1, 2, 3, 4, 5}

# Intersection
set1.intersection_update(set2)  # set1 becomes {3, 4, 5}

# Difference
set1.difference_update(set2)  # set1 becomes {1, 2}

# Symmetric Difference
set1.symmetric_difference_update(set2)  # set1 becomes {1, 2, 4, 5}


#cleR
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()  # fruits becomes set()
print(fruits)

#copy
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)


frozen = frozenset([1, 2, 3, 4])
# Attempting to add or remove elements will raise an error
frozen.append(5)
'''To maintain the immutability of frozenset, you cannot use methods like append, add, or remove. If you need to create a
 new set with additional elements, you can combine frozenset with other sets or frozensets:'''
frozen = frozenset([1, 2, 3, 4])
new_set = frozen | frozenset([5])
print(new_set)  # Output: frozenset({1, 2, 3, 4, 5})


squared_set = {x**2 for x in range(10)}
print(squared_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}


