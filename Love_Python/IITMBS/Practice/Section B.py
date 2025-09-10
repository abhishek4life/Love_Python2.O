#Question 1
def sum_of_squares_of_even(nums: list) -> int:
    '''Return the sum of squares of all even numbers in the list.

    Args:
        nums : list - list of integers

    Returns:
        int - sum of squares of all even numbers
    '''
#Answer 1
    return sum(x ** 2 for x in nums if x % 2 == 0)
#----------------------------------------------------------------------
#Question 2
'''Write a program that takes a passage with n lines of text as input. For each line, convert all vowels (a, e, i, o, u)
 to uppercase and all other characters to lowercase.'''
#Answer 2
# Number of lines
n = int(input())

# Define vowels
vowels = 'aeiou'

# Process and print each line
for _ in range(n):
    line = input()
    processed_line = ''.join([char.upper() if char in vowels else char.lower() for char in line])
    print(processed_line)

#-------------------------------------------------------------------------
#Question 3
def count_positive_ignore_none(nums: list):
    '''
    Count the number of positive integers in the list, ignoring `None` values and zeros.

    Args:
        nums (list): A list of numbers, possibly containing `None` values.

    Returns:
        int: The count of positive integers in the list.
    '''
#Answer 3
    return sum(1 for x in nums if x is not None and x > 0)
#-----------------------------------------------------------------------
#Question 4
'''Find Sum and Absolute Difference Alternately
Given n pairs of integers, print the sum and the absolute difference of each pair alternatively, starting with the sum
 for the first pair.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format
    • The first line contains an integer n, the number of pairs.
    • The next n lines each contain two comma-separated integers.

Output Format
    • For each pair of integers, print the sum if it is an odd-numbered pair (starting from 1), and
     the absolute difference if it is an even-numbered pair.'''
#Answer 4
# Read the number of pairs
n = int(input())

# Process each pair
for i in range(1, n + 1):
    x, y = map(int, input().split(','))
    result = x + y if i % 2 != 0 else abs(x - y)
    print(result)
#---------------------------------------------------------------------------------------
#Question 5
def last_word_starts_with_upper_case(sentence: str):
    """
    Find the last word in a sentence that starts with an uppercase letter.

    Args:
        sentence (str): The input sentence.

    Returns:
        str or None: The last word starting with an uppercase letter, or None if no such word exists.
    """
#Answer 5
    words = sentence.split()
    for word in reversed(words):
        if word and word[0].isupper():
            return word
    return None
#-------------------------------------------------------------------------------------
#Question 6
'''Swap Every Alternate Line and Reverse Odd Lines

Given multiple lines of input, modify the lines as follows:
    • Swap every two consecutive lines.
    • Reverse every odd-numbered line in the output sequence.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format:
    • The first line contains the integer n, the number of lines.
    • The next n lines contain text strings.

Output Format:
    • Print the transformed lines according to the rules specified'''
#Answer 6
# Number of lines
n = int(input())

# Read and process lines
lines = [input() for _ in range(n)]
for i in range(0, n - 1, 2):
    lines[i], lines[i+1] = lines[i+1], lines[i]
for i in range(n):
    if i % 2 == 0:
        lines[i] = lines[i][::-1]

# Print the transformed lines
for line in lines:
    print(line)


