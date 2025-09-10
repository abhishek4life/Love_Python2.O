# The try and except blocks are tools in Python that help manage
# exceptions (errors) during program execution, allowing the code
# to handle errors gracefully without crashing.

'''try Block: This block contains code that might raise an exception.
If the code runs successfully, the program skips the except block and continues.'''

'''except Block: If an error occurs in the try block, the program jumps to the except block. 
Here, we can define how to handle specific exceptions, like ValueError'''

'''What is a ValueError?: This occurs when a function receives a value of the correct data type but an inappropriate value.
 For example, attempting int("hello") raises a ValueError, as the string "hello" cannot be converted to an integer.'''

'''Using pass: In some cases, we may not need to take any action for the exception. The pass statement is used in the except 
block to skip the error and continue execution.'''

'''
with open('file.txt', 'r') as file:
    for line in file:
        try:
            number = int(line.strip())  # Convert to integer
            print(f"Valid number: {number}")
        except ValueError:
            pass  # Ignore invalid lines
'''
#input
# 42
# hello
# 56
# invalid

#output
# Valid number: 42
# Valid number: 56

# This approach ensures the program continues processing, skipping invalid lines smoothly.
# It’s essential for robust error handling in data processing scenarios

