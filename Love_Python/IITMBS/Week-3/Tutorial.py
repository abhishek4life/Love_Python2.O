#computing Factorialn
print("Factorail")
num=int(input("Enter a number:"))
Fact=1
if(num<0):
    print("Not Defined")
else:
    while(num>0):
        Fact=Fact*num
        num=num-1
    print(Fact)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Find whether the entered number is pallindrome
# Original number
number = 12321
original_number = number

# Reverse the number
reversed_number = 0
while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

# Check if the original number and reversed number are the same
if original_number == reversed_number:
    print(f'{original_number} is a palindrome.')
else:
    print(f'{original_number} is not a palindrome.')
