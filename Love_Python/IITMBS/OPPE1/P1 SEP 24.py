def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    '''
    Given three side lengths in the increasing
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.

    Arguments:
    a: int - the first side length
    b: int - the second side length
    c: int - the hypotenuse length

    Return:
    bool - True if the sides form a right triangle and the perpendicular sides are even, else False
    '''
    ...

def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    '''
    Given a string, check if all the odd indices are alphabets and the even indices are digits.

    Note: indices starts from 0.

    Arguments:
    string: str - the input string

    Return:
    bool - True if all odd indices are alphabets and even indices are digits, else False
    '''
    ...

def swap_even_and_odd_indices(l: list) -> None:
    '''
    Given a list of integers, swap the values at the even indices
    and the odd indices by modifying the same list.

    Arguments:
    l: list - the input list of integers

    Return:
    None - the input list is modified inside the function.
    '''
    ...

def unique_chars_present_in_first_not_in_second(s1: str, s2: str) -> set:
    '''
    Given two words as strings, find the unique
    chars that are present in the first word but not in
    the second word.

    Assume all characters in the input are in lowercase.

    The order of elements in the set doesn't matter while returning.

    Eg. water, watch -> {'e','r'}

    Arguments:
    s1: str - the first string
    s2: str - the second string

    Return:
    set - the unique characters present in the first string but not in the second string
    '''
    ...

def repeat(t: tuple) -> tuple:
    '''
    Given a tuple of length two, say (a,b), create a tuple
    with a repeated b number of times and b repeated a number of times.

    E.g., repeat((2, 3)) ->  (2, 2, 2, 3, 3)

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a new tuple with a repeated b times followed by b repeated a times
    '''
    ...

def num_squares(n: int) -> dict:
    '''
    Given an integer n, create a dictionary with the
    numbers from 1 to n (inclusive) as keys and their
    squares as values.

    Arguments:
    n: int - the input integer

    Return:
    dict - the dictionary with numbers from 1 to n as keys and their squares as values
    '''
    ...
