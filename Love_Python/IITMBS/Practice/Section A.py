#Question 1
from tkinter.messagebox import QUESTION


def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    '''Return the sum of squares and the absolute difference of squares.
    Args:
        a, b : int - input numbers
    Returns:
        tuple - tuple with sum of squares and absolute difference of squares.
    '''
#Answer 1
    return (a**2+b**2, abs(a**2-b**2))


print(sum_squares_abs_diff_squares(3, 4))  # Output should be (25, 7)

#------------------------------------------------------------------------------------
#Question 2
def is_odd_length_palindrome(s: str) -> bool:
    '''Check if a string is a palindrome with odd length.
    Args:
        s : str - input string
    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
    '''
#Answer 2
     #return s == s[::-1] and len(s) % 2 == 0
    if s[::-1]==s and len(s)%2==1:
        return True
    return False

print(is_odd_length_palindrome("non"))
#--------------------------------------------------------------------------
#Question 3
def remove_elements_at_two_indices(l: list, i1: int, i2: int):
    '''Remove elements at two specified indices in the list.
    Args:
        l : list - input list
        i1, i2 : int - indices of elements to remove
            both are non-negative and unique
    Returns:
        None - modifies the list in place
    '''
#Answer 3
    #for i in sorted([i1, i2], reverse=True):
        #l.pop(i)
    #----------------------------------------
    # Ensure i1 is smaller than i2 to remove elements without affecting indices
    if i1 > i2:
        i1, i2 = i2, i1

    del l[i2]
    del l[i1]


# Sample list and indices
sample_list = [10, 20, 30, 40, 50]
index1 = 1  # Index of element to remove
index2 = 3  # Index of element to remove
print(sample_list)  # Expected output: [10, 30, 50]
#----------------------------------------------------------------------------
#Question 4
def is_positive_odd_or_negative_even(n: int) -> bool:
    '''Check if the number is a positive odd or a negative even.
    Args:
        n : int - input integer
    Returns:
        bool - True if positive odd or negative even, else False
    '''
#Answer 4
    return (n > 0 and n % 2 == 1) or (n < 0 and n % 2 == 0)
#----------------------------------------------------------------------------
#QUESTION 5
def within_and_has_double_quotes(s: str) -> bool:
    '''Check if the string is enclosed with double quotes and has double quotes inside.

    Args:
        s : str - input string

    Returns:
        bool - True if the string starts and ends with double quotes and has double quotes inside
    '''
#Answer 5
    # Check if the string starts and ends with double quotes
    if s.startswith('"') and s.endswith('"'):
        # Check if the string contains double quotes inside
        inner_string = s[1:-1]  # Remove the enclosing double quotes
        if '"' in inner_string:
            return True
    return False
#------------------------------------------------------------------------------
#QUESTION 6
def div_by_exactly_one(num: int, a: int, b: int) -> bool:
    '''Check if num is divisible by exactly one of a or b.

    Args:
        num, a, b : int - input numbers

    Returns:
        bool - True if num is divisible by exactly one of a or b, otherwise False.
    '''
#Answer 5
    # Check if num is divisible by a
    divisible_by_a = (num % a == 0)

    # Check if num is divisible by b
    divisible_by_b = (num % b == 0)

    # Return True if num is divisible by exactly one of a or b
    return divisible_by_a != divisible_by_b

#------------------------------------------------------------------------------
#Qouestion 7
def mm_dd_yy_to_yy_dd_mm(date: str) -> str:
    """
    Convert a date string from the format mm-dd-yy to yy-dd-mm.

    Args:
        date (str): The date in the format "mm-dd-yy".

    Returns:
        str: The date in the format "yy-dd-mm".

    Example:
        >>> mm_dd_yy_to_yy_dd_mm("12-25-21")
        "21-25-12"
    """
#Answer 7
    # Split the date string into parts
    parts = date.split('-')
    month, day, year = parts[0], parts[1], parts[2]

    # Reformat the date string to yy-dd-mm
    new_date = f"{year}-{day}-{month}"

    return new_date
#---------------------------------------------------------------------------
#Ouestionn 8
def increment_value_with_max_limit(d: dict, key: str, inc: int, limit: int):
    '''
    Increment the value for the given key in the
    dictionary by `inc`, but not beyond `limit`.

    Modify the value in the dictionary do not return the new value.

    Args:
        d : dict - dictionary with integer values
        key : str - key to increment in the dictionary
        inc : int - increment value
        limit : int - maximum limit for the value

    Returns:
        None
    '''
#Answer 8
    if key in d:
        d[key] = min(d[key] + inc, limit)
    else:
        d[key] = min(inc, limit)
#---------------------------------------------------------------------------