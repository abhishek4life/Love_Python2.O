

x='pytHon sTrIng mEthOdS'
print(x.lower())
print(x.upper())
print(x.title())
print(x.capitalize())
print(x.swapcase())

#print("Check Lower",input(islower())) #cannot use directly in input function

user_input = input("Enter a string: ")  # Prompt the user for input
if user_input.islower():  # Check if the input is in lowercase
    print("Check Lower:", user_input)  # Print the input if it is in lowercase
else:
    print("The input is not in lowercase.")  # Print a message if it is not in lowercase

a="abhishek"
print(a.isupper())

# Similarly For
'''
x.isupper()
x.title()
x.capitalize()
x.isdigit()
x.isalpha()
x.isalnum()
#################################
x.startwith('') # case sensitive
x.endwith('') # case sensitive
x.count('')
x.index('')
x.replace('','')
'''

y='----Python----'
print(y.strip('-'))
print(y.lstrip('-'))
print(y.rstrip('-'))