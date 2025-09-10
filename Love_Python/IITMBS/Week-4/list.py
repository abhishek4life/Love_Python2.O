
'''A list in Python is an ordered collection of items (elements) that can be of different data
types like numbers, strings, or even other lists. Lists are very versatile and can be used to
store a sequence of elements which you can iterate through, modify, and access by index.'''

#l.remove , remove first occurrence
#contain list of list or array of array

my_list = [1, 2, 3, 'hello', 4.5] #creation
print(my_list[1:3])  # Output: [2, 3] #slicing
print(my_list[0])  # Output: 1 #indexing
my_list.append(6) #appending
print(my_list)
my_list.insert(1, 'world') #inserting
print(my_list)
my_list.remove('hello') #remove
print(my_list)
popped_item = my_list.pop(2) #remove
print(popped_item)
print(my_list)
print(len(my_list))  # Output: 5 (if 'hello' is removed and 'world' is inserted)


print("concatenation")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list1 = list1 + list2
combined_list2 = list2 + list1
print(combined_list1,combined_list2)

#repetation
repeated_list = list1 * 3  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#comparing
print([1,2]<[2,1])  #0th pxn
print([1]<[1,2,3])
print([]<[1])

#mutable
l=[1,2,4]
l[2]=3
print(l)

s='abce'
#s[3]='d'
#print(s) #error, string is immutable identity in python


#swapping variable
x = 5
y = x
x=10
print(x,y) #10 5

l1=[1,2,3]
l2=l1
l1[0] = 100
print(l1,l2) # [100,2,3] [100,2,3]
'''12 = 11 makes 12 refer to the same list object as 11 . Essentially, 12 is another
name for the same list.
When you update 1110] to 100 , it modifies the first element of the list that both
11 and 12 refer to.
Consequently, both 11 and 121 reflect the change, resulting in [100, 2, 3] for
both.'''


l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()

l2[0]=100
l3[1]=200
l4[2]=300

print(l1,l2,l3,l4)

#Two diffrent variable at same memory location
print(l1 is l2)
print(l1 is l3)
print(l1 is l4)


#inserting
k=[1,2,3,4,5]
k.insert(2,9)
print("k=",k)

#list comprehension
squared_list = [x**2 for x in range(10)]  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Output: [0, 4, 16, 36, 64]

#sorting
unsorted_list = [3, 1, 4, 1, 5, 9]
unsorted_list.sort()  # In-place sorting
sorted_list = sorted(unsorted_list)  # Return a new sorted list
print("sorted_list:",sorted_list)

#Reversing
my_list.reverse()  # In-place reversal
reversed_list = my_list[::-1]  # Return a new reversed list
print("resversed_list",reversed_list)

#Copying
copied_list = my_list.copy()
another_copy = my_list[:]

#removing
#l.remove(element)
#l.pop(index)

#clearing
my_list.clear()  # Now my_list is an empty list

#Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Output: 6


#iterating Through list
for item in my_list:
    print(item)

#list membership
if 3 in my_list:
    print("3 is in the list")


