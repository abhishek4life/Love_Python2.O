'''Check if a given element k is present in a list'''

def obvious_search(L, K):
    for x in L:
        if x == K:
            return 1
    return 0

L=list(range(25))
#print(L)
print(obvious_search(L,7))
#--------------------------------
def sum(n):
    ans=0
    for i in range(n):
        ans=ans+i
    return ans

print(sum(10))
#--------------------------------
import time
print(time.time()) #time in second since Epoch

a=time.time();print(sum(100));b=time.time();print(b-a)
print(a)
print(b-a)

#------------------------------
#(begin+end)//2 gives us the mid point of the list starting from begin and ending in end
'''

- **Introduction to Binary Search**: The video starts with a warm-up for binary search, explaining its significance in
    searching algorithms.
- **Obvious Search**: Initially, a straightforward linear search algorithm is demonstrated, where each element in a list 
    is checked sequentially to find a specific element. This method, while simple, becomes inefficient for large lists.

- **Time Measurement**: The video then delves into measuring the execution time of functions using Python's `time` module.
 Examples include calculating the sum of numbers and observing how the time taken increases with the size of the list.

- **Midpoint Calculation**: A key concept introduced is finding the midpoint of a list, which is crucial for binary search.
 This is done by calculating `(begin + end) // 2`, where `begin` and `end` are the indices of the list's start and end.

- **Binary Search Concept**: Although not fully implemented in the video, the groundwork for binary search is laid out. 
The idea is to repeatedly divide the search interval in half, which significantly reduces the number of elements to check, 
making it much faster than linear search for large, sorted lists.

- **Efficiency Discussion**: The video highlights the inefficiency of linear search for large lists, especially when 
searching for elements not present or at the end of the list, setting the stage for introducing binary search as a more
 efficient alternative.

- **Future Content**: The video promises to explore binary search in detail in subsequent lectures, using real-world examples 
like finding a word in a dictionary or halving a number to quickly reach zero or a single digit.

This video serves as an educational piece, preparing viewers for understanding and implementing binary search by first illustrating 
the limitations of linear search and introducing foundational concepts like time measurement and midpoint calculation[1].

'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Binary Search Implementation

def binary_search(lst, key):
    """
    This function efficiently searches for a key in a sorted list using the binary search algorithm.
    Returns 1 if the key is found, otherwise returns 0.
    """
    begin = 0  # First element index
    end = len(lst) - 1  # Last element index

    while begin <= end:  # Loop until the search space is exhausted
        mid = (begin + end) // 2  # Compute the middle index

        if lst[mid] == key:  # Check if the middle element is the key
            return 1
        elif lst[mid] > key:  # If the key is smaller, search the left half
            end = mid - 1
        else:  # If the key is larger, search the right half
            begin = mid + 1

    return 0  # Key was not found

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

- **Introduction to Binary Search Recursion**: The video starts with the instructor planning to write a recursive binary 
search algorithm. The goal is to find an element $$ k $$ in a sorted list $$ L $$ by recursively narrowing down the search space.

- **Algorithm Development**: 
  - The instructor outlines the basic structure of the recursive function, which takes the list $$ L $$, the element to search 
  $$ k $$, and the start and end indices of the current search region.
  - **Trivial Cases**: 
    - If `begin` equals `end`, check if the element at `begin` is $$ k $$. If true, return 1; otherwise, return 0.
    - If `end - begin` equals 1, check both `begin` and `end` for $$ k $$. If found, return 1; otherwise, return 0.
  - **General Case**: 
    - Compute the middle index `mid` as `(begin + end) // 2`.
    - If $$ L[mid] $$ is greater than $$ k $$, discard the right half and retain the left half by setting `end = mid - 1`.
    - If $$ L[mid] $$ is less than $$ k $$, discard the left half and retain the right half by setting `begin = mid + 1`.
    - If $$ L[mid] $$ equals $$ k $$, return 1 as the element is found.

- **Error Handling**: The instructor mentions potential errors due to incomplete code and discusses how to handle cases 
where `end - begin` becomes negative, indicating no region of interest left, and thus returning 0.

- **Performance**: The video demonstrates the efficiency of the recursive binary search by comparing it with a linear 
search, showing how quickly it can find or confirm the absence of an element in large lists.

- **Limitations of Recursion**: A brief discussion on the limitations of recursion in Python, particularly the default
 recursion depth limit of 999, is included. This limit can be changed, but there's a caution about the potential for 
 infinite recursion if not managed properly.

- **Conclusion**: The instructor emphasizes the importance of practice in understanding and implementing recursive 
algorithms, likening the process to looking up a word in a dictionary by halving the search space repeatedly.

The video concludes with a reminder to practice coding and a note on the dangers of recursion, particularly in Python, 
due to its default recursion depth limit.

'''