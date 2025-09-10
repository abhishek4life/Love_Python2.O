n = int(input("Enter an integer: "))

# Upper part of the diamond
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)

# Lower part of the diamond
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)


#-----------------------------------------------


# Pattern Printing - Diamond (Odd n)
n = int(input("Enter an odd number: "))

# Upper part of the diamond
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)

# Lower part of the diamond
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)


#--------------------------------------------------


# Pattern Printing - Diamond (Even n)
n = int(input("Enter an even number: "))

half = n // 2

# Upper part of the diamond
for i in range(1, half + 1):
    print(" " * (half - i) + "*" * (2 * i - 1))

# Lower part of the diamond
for i in range(half, 0, -1):
    print(" " * (half - i) + "*" * (2 * i - 1))


#---------------------------------------------------------

