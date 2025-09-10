def sums(n):
    ans=0
    for i in range(n):
        ans=ans+(i+1)
    return ans

#recursion in python

def sum(n):
    if (n==1):
        return 1
    else:
        return n+sum(n-1) #fn inside fn

# python let you call the same fn within fn

#ci intrest 10%
def comp(p,n):
    if (n==1):
        return p(1.1)
    else:
        return (comp(p,n-1)*1.1)

def fact(n):
    if (n==1):
        return 1
    else:
        return (fact(n-1))*1.1

# To check 0 in the list
def check0(l):
    if len(l) == 0:  # Base case: if the list is empty
        return 0  # False
    if l[0] == 0:  # Check if the first element is 0
        return 1  # True
    else:
        return check0(l[1:])  # Recursively call with the rest of the list

print(check0([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # This will correctly return 1
# this is not a efficient code

#9.6
# Finds the minimum element in the list L
def mini(L):
    min_val = L[0]  # Initialize to the first element
    for x in L:
        if x < min_val:
            min_val = x
    return min_val

# Recursively sorts the list L
def Sort(L):
    if not L:  # Base case: if the list is empty, return an empty list
        return []
    m = mini(L)
    L.remove(m)
    return [m] + Sort(L)  # Recursive call
