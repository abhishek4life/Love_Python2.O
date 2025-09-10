def is_num_sorted(num)->bool:
    '''
    Check if a number is sorted.
    sorted means the digits of a number are sorted in ascending order.
    Eg. 1468 - sorted , 4948 - not sorted.

    Argument: num: int
    Return: bool
    '''

    num_str = str(num)
    num_str_sorted = "".join(sorted(list(num_str)))
    return num_str == num_str_sorted

def sorted_num_count(nums:list) -> int:
    '''
    Given a list of nums(int) find the count of sorted numbers in the list.

    Arguments: nums - list[int]
    Return: count - int
    '''

    return len(list(filter(is_num_sorted, nums)))
    # another approach - can also use comprehensions
    # return sum(map(well_behaved, nums)) # sum of boolean will be the count

def common_substring(words:list)->str:
    '''
    Given a list of words check whether there is a word in words
    that is a substring of all other words.
    If there is a word return that word else return None

    Hint: only the smallest word can be a substring of all other words.

    Arguments: words - list[str]
    Return: common_substr_word - str
    '''

    min_word = min(words, key = len)
    # check if min_word in word for all word in words
    if all(map(lambda word : min_word in word, words)):
        return min_word
    # another approach using comprehensions
    # if all(min_word in word for word in words):
    #     return min_word

def is_valid_phone_number(phone_no:int)->bool:
    '''
    Check if a number is valid for a specific operator.

    A phone number is valid if
        - it has 10 digits
        - should begin with 98123
        - same digit should not occur more that 5 times.
    '''

    phone_no_str = str(phone_no)
    # note that the below return statement is a single experssion
    return (
        len(phone_no_str) == 10 # has 10 digits
        and phone_no_str[:5] == "98123" # begins with 98123
        and all(phone_no_str.count(str(digit))<=5 for digit in range(0,10)) # check if all the numbers are present less than 5 times
    )

def validate_phone_numbers(phone_nos:list)->dict:
    '''
    Given a list of phone numbers, create a dict with
    phone numbers as keys and the string "VALID" or "INVALID"
    depending on the validity of the phone number as described by the above funtion.

    Arguments: phone_nos - list
    Return: validity_dict - dict[int,str]
    '''

    return {
        number: "VALID" if is_valid_phone_number(number) else "INVALID"
        for number in phone_nos
    }

def get_election_winner(votes:dict)->str:
    '''
    Given a dictionary with candidate name as key and number of votes as values,
    Find the winner of the election who has the maximum votes

    Arguments: votes - dict[str, int]
    Return: winner - str
    '''

    return max(votes, key = votes.get)

def misspelt_words(vocab:str, sentence:str)->list:
    '''
    Given a comma separated string of vocabulary,
    and a space separated string sentence,
    return a list of misspelt words in the order they occur in the sentence.

    The words which are not in the vocabulary are considered misspelt.

    Arguments:
        vocab - str: comma separated string with vocabulary
        sentence - str: space separated string of sentence
    Return:
        misspelt_words - list
    '''

    vocab, words = set(vocab.split(",")), sentence.split()
    return [word for word in words if word not in vocab]

    # another approach
    # return list(filter(lambda x: word not in vocab, words))

def count_sock_pairs(sock_colors:list)->int:
    '''
    Given a list of sock colors representing the color of each sock,
    find the number of sock pair (both having same color) is there.
    Eg. ["red","blue","green","green","red","green","red","red","blue","black"]
    2 red+ 1 green+ 1 blue = 5 pairs

    Arguments: sock_colors - list: of sock colors
    Return: number of pairs of sock - int
    '''

    sock_counts = {}
    # count socks of each color
    for color in sock_colors:
        if color not in sock_counts:
            sock_counts[color] = 0
        sock_counts[color] += 1
    # use floor division to find the number of sock pairs
    return sum(count//2 for count in sock_counts.values())

def is_vowely(word:str)->bool:
    '''
    Check if a given word is vowely. A word is vowely if
    - it has all the vowels in it.
    - the vowels occur in ascending order.

    Assume no letter repeats in the given word.

    Eg. abecidofu - vowely, tripe - not vowely, eviaoqu - not vowely

    Argument: word - a string with no letter repeated
    Return: bool

    Hint: if the non-vowels are removed from the word, it would be just aeiou
    '''

    return "".join(char for char in word if char in "aeiou" ) == "aeiou"
    # alternate approach using filter
    # return "".join(filter(lambda char: char in "aeiou", word)) == "aeiou"

def vowely_count(words:list)->int:
    '''
    Given a list of words find the number of vowely words from the list.

    Arguments: words :list[str]

    Return: int - number of vowely words
    '''

    return len(list(filter(is_vowely, words)))

def format_name(first:str, middle:str, last:str)->str:
    '''
    Given three lower case parts of name,
    return the full name with first letter capitalized in each part.

    Note that middle name can be empty.
    '''

    first, middle, last = map(str.title, (first, middle, last))
    return f"{first} {middle} {last}" if middle else f"{first} {last}"

def double_palindromes(n:int)->list:
    '''
    Given a number n, find all the positive integers till n (including)
    that are double_palindrome. A number is double palindrome if
    it is a palindrome and its square is a palindrome.

    Eg.
    8 - palindrome, not double palindrome
    11 - palindrome and double palindrome
    12 - not palindrome and not double palindrome

    Arguments: n - int: range of numbers to search
    Return: list of integers which are double palindrome in the ascending order
    '''

    def is_palindrome(n):
        n_str = str(n)
        return n_str==n_str[::-1]
    return list(filter(lambda x: is_palindrome(x) and is_palindrome(x**2), range(1,n+1)))
    # alternate approach using comprehensions
    '''
    return [
        num for num in range(1,n+1)
        if is_palindrome(x) and is_palindrome(x**2)
    ]
    '''

def scores_spx(kakashi_moves:list, guy_moves:list):
    '''
    Given the series of moves played by Kakashi and Guy in a Stone-Paper-Scissor game,
    find the scores of Kakashi and guy respectively.
    Rules - Stone beats Scissor, Scissor beats Paper and Paper beats Stone
    Score - Number of times won
    Symbols - Stone - S, Paper - P, Scissor - X

    Arguments:
    kakashi_moves and guy_moves - list of moves where each move
        is a string corresponding to the symbol

    Return: kakashi_score:int , guy_score:int
    '''

    wins = [('S','X'), ('X','P'),('P','S')]

    k_score, g_score = 0,0
    for k, g in zip(kakashi_moves, guy_moves):
        if (k,g) in wins:
            k_score+=1
        elif (g,k) in wins:
            g_score+=1

    return k_score, g_score