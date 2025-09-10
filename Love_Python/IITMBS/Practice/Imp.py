day = 15       # Example day
month = 3      # Example month (March)
year = 2025    # Example year

# Add 10 months
month += 10   # month becomes 13

# Adjust month and year
# month-1 = 12, (12%12) = 0, 0+1 = 1 (January)
# year + (12//12) = 2025 + 1 = 2026
month, year = (month-1)%12+1, year+(month-1)//12

# Format the new date
tenth_month = str(day) + "/" + str(month) + "/" + str(year)

print(f"Date after 10 months: {tenth_month}")
#--------------------------------------------------------------------------------
time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM)
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)


 # bool: True if time is valid (should be ranging from 1 - 12 both including) else False
is_time_valid = 0 < int(time[:2]) <= 12

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = int(time[:2])%12 + (time[-2:] == "PM") * 12

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here
if not is_time_valid:
    time_of_day = "Invalid"
elif 0 <= time_in_hrs < 6:
    time_of_day = "Night"
elif 6<= time_in_hrs < 12:
    time_of_day = "Morning"
elif 12<= time_in_hrs < 18:
    time_of_day = "Afternoon"
elif 18<= time_in_hrs < 24: # you could also use else here.
    time_of_day = "Evening"

#--------------------------------------------------------------------------------------
def palindrominator:
    # Palindrominator
    string = input("Type:")
    palindrome = string + string[-2::-1] #For string = "abc", this results in: "abc" + "ba" which is "abcba".
    print(palindrome)

def simple_interest:
    # Simple interest calculator
    principal_amount = float(input("Type Amount:"))
    n_years = int(input("Type Year:"))
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = principal_amount * interest_rate * n_years
    print(int(simple_interest))

else:
    print("Invalid Operation")

def vowel_check:
    # Vowel checker
    string = input().lower()
    if ("a" in string or "e" in string or "i" in string or "o" in string or "u" in string) :
        print("yes")
    else:
        print("no")
#-------------------------------------------------------------------------------------------
print("Shift by 1 letter")
name = "abhishek"
alpha = "abcdefghijklmnopqrstuvwxyz"
shifted_name = ""
k = 1  # Shift a letter by k

for i in range(len(name)):
    shifted_name += alpha[((alpha.index(name[i]) + k) % 26)]

print(shifted_name)

#-----------------------------------------------------------------------------------------------
import math
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(10,3))

import random
print(random.random()) #between 0 and 1

# let us simulate a coin toss
a=random.random()
if (a<.5):
    print("Head")
else:
    print("Tail")

# let us simulate a dice six face
print(random.randrange(1,7))
#-------------------------------------------------------------------------------------------------
#left align
print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))
#right align
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

#------------------------------------------------------------------------------------------------
print("Prime Number less than entered number")
num= int(input("Enter number:"))
if (num>2):
    print(2,end=' ')#in the same line

for i in range (3,num): # range of outer loop
    flag=False
    for j in range (2,i): #range of inner for loop
        if (i%j==0): #if satisfied then it is not prime number
            flag=False
            break # break inner loop
        else:
            flag=True
    if (flag):
        print(i,end=' ')

#-----------------------------------------------------------------------------------------------

#Number of digit in a given number
print("Number of digit")
print("using string conversion")

number=int(input("Enter a number:"))
n=len(str(abs(number)))
print(n)
#------------------------------------------------------------
print("Number of digit")
print("using loop")
number=abs(int(input("Enter a number:")))
digit=1 #lowest possible value
while (number>9):
    number=number//10 #given number 1234-->123-->12-->1 and digit each time increamented
    digit=digit+1
    #print(digit) #getting repeated value
print(digit)

#Comparison:
#The first approach is more concise and leverages Python's string manipulation functions.
#The second approach is more algorithmic and gives a deeper understanding of how the process works.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Reverse the digits in the given number
print("Reverse Digit")
print("using string conversion")
alpha = abs(int(input("Enter the number: ")))  # Taking input and making it positive if negative
alpha1 = str(alpha)  # Converting the number to a string
reverse = alpha1[::-1]  # Reversing the string
print(reverse)  # Printing the reversed string
#----------------------------------------------------------------------------

print("Reverse Digit")
print("using loop")
number = abs(int(input("Enter the number: ")))  # Taking input and making it positive if negative
reverse = 0  # Initialize the reversed number as 0

while number > 0:
    remainder = number % 10  # Get the last digit
    reverse = (reverse * 10) + remainder  # Add the last digit to the reversed number
    number = number // 10  # Remove the last digit from the original number

print(reverse)  # Print the reversed number

#---------------------------------------------------------------------------------
def find_min:
    n = int(input())
    minimum = int(input())
    for i in range(n-1):
        current = int(input())
        if current< minimum:
            minimum = current
    print(minimum)

#---------------------------------------------------------------------------------
empty_set = set()
singleton_tuple = (1,)
_falsy_list = [] # list: a list but when passed to bool function should return False.
a_falsy_set = set() # set: a list but when passed to bool function should return False.
a_truthy_tuple = (1,2,3) # tuple: a tuple but when passed to bool function should return True

int_iterable = range(1,10,3)

int_iterable_min = min(int_iterable) # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max = max(int_iterable) # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = sum(int_iterable) # int: you know what to do
int_iterable_len = len(int_iterable) # int: really... you need hint?
int_iterable_sorted = sorted(int_iterable) # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = sorted(int_iterable,reverse=True) # list: the int_iterable sorted in desc order

'''If the input is not a set, it simply reverses the input.
If the input is a set, it sorts the input in descending order.'''
'''
isinstance(object, classinfo)
Multiple Type Checking
value = 3.14
print(isinstance(value, (int, float)))  # Output: True
'''

if not isinstance(int_iterable,set) : # some iterables are not reversible why?
    int_iterable_reversed = list(reversed(int_iterable)) # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = sorted(int_iterable,reverse=True) #list
print("int_iterable_reversed",int_iterable_reversed)

#------------------------------------------------------------------------------------------------
def list_mutating_operations(items:list, item1, item2):
    # sort the `items` inplace
    items.sort()
    print("sorted:",items)

    # add item1 to the `items` at the end
    items.append(item1)
    print("append:",items)

    # add item2 at index 3
    items.insert(3,item2)
    print("insert:",items)

    # extend `items` with the first three elements in `items`
    items.extend(items[:3])
    print("extend:", items)

    # pop the fifth element and store it in variable `popped_item`
    popped_item = items.pop(4)
    print("pop:",items)

    # remove first occurance of `item2` from the list
    items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    items[4] = None
    print("modify_index:",items)

    # make the even indices None
    items[::2] = [None]*len(items[::2])
    print("modify_slice:",items)

    # delete the third last element
    del items[-3]
    print("delete_index:",items)

    # delete the even indices
    del items[::2]
    print("delete_slice:",items)

    return items, popped_item

def list_non_mutating_operations(items:list, item1, item2):

    # print the sorted version of items
    print("sorted:",sorted(items))

    # print a lsit with item1 appended to the `items` at the end
    print("append:",items+[item1])

    # print a list with item2 added to items at index 3
    print("insert:",items[:3]+[item2]+items[3:])

    # print a list with the first three elements in `items` added to the end of the `items` again
    print("extend:", items+items[:3])

    #  print a list with the fifth element from `items` removed
    print("pop:",items[:4]+items[5:])

    # print a list with first occurance of `item2` removed from `items`
    index = items.index(item2)
    print("remove:",items[:index]+items[index+1:]) # hint: you may want to use index

    # print a list with the fourth element of `items` changed to None
    print("modify_index:",items[:3]+[None]+items[4:])

    # print a list with the even indices changed to None
    modified = items[::] # make a copy or use items.copy()
    modified[::2] = [None]*len(modified[::2])
    print("modify_slice:",modified)

    # print a list with the even indices removed
    print("delete_slice:",modified[1::2])

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))
    # remove item2 from set1. What if item2 is not in set1?
    set1.discard(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2 & set3))

    # print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1 | set2 | set3))

    # print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2 - set3))

    # print all the non common elements from both set2 and set3
    print(sorted(set2.symmetric_difference(set3)))

    return set1,sorted(set1),sorted(set2),sorted(set3)

#-------------------------------------------------------------------------------------------------
def swap_halves(items):

    m = len(items)//2
    return items[m:]+items[:m]

def swap_at_index(items,k):

    return items[k+1:] + items[:k+1]

def rotate_k(items,k=1):

    k = k % len(items)
    return items[-k:]+items[:-k]

def first_and_last_index(items,elem):

    return items.index(elem), len(items)-1-items[::-1].index(elem)

def reverse_first_and_last_halves(items):

    m = len(items)//2
    items[:m], items[m:] = items[:m][::-1], items[m:][::-1]

#-----------------------------------------------------------------------------------------
def sum_of_squares(numbers):

    return sum([num**2 for num in numbers])

def total_cost(cart):

    return sum([quantity*price for quantity, price in cart])

def abbreviation(sentence):

    return ".".join([word[0].upper() for word in sentence.split()])+"."

def palindromes(words):

    return [word for word in words if word == word[::-1]]

def all_chars_from_big_words(sentence):

    return {
        letter.lower()
        for word in sentence.split()
        for letter in word
        if len(word)>5
    }

def flatten(lol):

    return [elem for row in lol for elem in row]

def unflatten(items, n_rows):

    n_cols = len(items)//n_rows
    return [
        [items[n_cols*j+i] for i in range(n_cols)]
        for j in range(n_rows)
    ]

def make_identity_matrix(m):

    return [
        [1 if i==j else 0 for i in range(m)]
        for j in range(m)
    ]

def make_lower_triangular_matrix(m):

    return [
        [i+1 if i<=j else 0 for i in range(m)]
        for j in range(m)
    ]
#----------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------
