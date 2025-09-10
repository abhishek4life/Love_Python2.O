'''Given a list of strings, check if all strings follow the format where the same word is repeated exactly twice with a hyphen in-between them. The word repeated should not be empty.

Examples of correct format:

"fast-fast" - correct
"go-go" - correct
"yeah-yeah" - correct
Examples of incorrect format:

"fast-slow" - incorrect (different words)
"fast-fast-fast" - incorrect (word repeated more than twice)
"fastfast" - incorrect (no hyphen)
"asfdadf" - incorrect (no hyphen, word not repeated)
"-" incorrect (empty word) '''

def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''
    ...