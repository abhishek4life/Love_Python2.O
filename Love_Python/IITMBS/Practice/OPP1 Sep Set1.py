def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    '''Return the sum of squares and the absolute difference of squares.

    Args:
        a, b : int - input numbers

    Returns:
        tuple - tuple with sum of squares and absolute difference of squares.

    '''
    return (a**2+b**2,abs(a**2-b**2))
print(sum_squares_abs_diff_squares(1,2))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def is_odd_length_palindrome(s: str) -> bool:
    '''Check if a string is a palindrome with odd length.

    Args:
        s : str - input string

    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
    '''
    return (len(s)%2!=0 and s==s[::-1])
print(is_odd_length_palindrome("racecar"))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def remove_elements_at_two_indices(l: list, i1: int, i2: int):
    '''Remove elements at two specified indices in the list.

    Args:
        l : list - input list
        i1, i2 : int - indices of elements to remove
            both are non-negative and unique

    Returns:
        None - modifies the list in place
    '''

    if i1>i2:
        l.pop(i1)
        l.pop(i2)
    else:
        l.pop(i2)
        l.pop(i1)
    return l
l=[1,2,3,4,5,6,7,8]
i1=3
i2=5

print(remove_elements_at_two_indices(l,i1,i2))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def sum_of_squares_of_even(nums: list) -> int:
    '''Return the sum of squares of all even numbers in the list.

    Args:
        nums : list - list of integers

    Returns:
        int - sum of squares of all even numbers
    '''

    even_squares = [num ** 2 for num in nums if num % 2 == 0]
    return sum(even_squares)

'''
even = [num for num in nums if num % 2 == 0]
    sq = sum(num ** 2 for num in even)
    return sq
    '''

nums=[1,2,3,4,5]
print(sum_of_squares_of_even(nums))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''Upper Case Only Vowels
Write a program that takes a passage with n lines of text as input. For each line, convert all vowels (a, e, i, o, u) to uppercase and all other characters to lowercase.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format
    • The first line contains an integer n, the number of lines.
    • The next n lines contain the passage.
Output Format
    • Print the passage with vowels in uppercase and all other characters in lowercase.'''

def processs_line(line):
    vowels='aeiou'
    result=''

    for char in line:
        if char.lower() in vowels:
            result += char.upper()
        else:
            result =+ char.lower()

    return result


n = int(input())
lines = [input() for _ in range(n)]

print()
for line in lines:
    print(process_line(line))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_roll_nos(data:list, criteria=None):
    '''
    Filter roll numbers based on criteria.

    Args:
        data (list): List of tuples with roll number and marks.
        criteria (str, optional): The criteria for filtering.

    Returns:
        list: List of roll numbers matching the criteria or None if invalid criteria.
    '''

        if criteria not in ['above_average', 'below_average', 'fail', 'toppers', None]:
            return None

        if not data:
            return []

        if criteria is None:
            return [roll_no for roll_no, _ in data]

        marks = [mark for _, mark in data]
        average = sum(marks) / len(marks)

        if criteria == 'above_average':
            return [roll_no for roll_no, mark in data if mark >= average]
        elif criteria == 'below_average':
            return [roll_no for roll_no, mark in data if mark < average]
        elif criteria == 'fail':
            return [roll_no for roll_no, mark in data if mark < 40]
        elif criteria == 'toppers':
            return [roll_no for roll_no, mark in data if mark >= 90]


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''Print Pattern - V
Given an integer n (where n > 0), print a "V" shaped pattern with n rows. 
The pattern should use backslashes (\) and forward slashes (/) for each row, 
with the v character at the bottom. There should be no spaces to the right of the pattern.

NOTE: This is an I/O type question, you need to write the whole code for 
taking input and printing the output.

Input Format
    • A single integer n, representing the number of rows in the pattern.

Output Format
    • A "V" shaped pattern with n rows, as described.'''

