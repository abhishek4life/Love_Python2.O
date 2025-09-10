#Pattern Printing - Hexagon
#Given an integer n as input, print a hexagon pattern with '@' having a side length of n.
n = int(input())

# Upper part of the hexagon
for i in range(n):
    print(" " * (n - i - 1) + "@" * (n + 2 * i))

# Lower part of the hexagon
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "@" * (n + 2 * i))


#ODD No
n = int(input("Enter an odd integer: "))

# Upper part of the hexagon
for i in range(n):
    print(" " * (n - i - 1) + "@" * (n + 2 * i))

# Lower part of the hexagon
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "@" * (n + 2 * i))


#even No
n = int(input("Enter an even integer: "))

# Proceed only if n is even
while n % 2 != 0:
    n = int(input("Please enter an even integer: "))

# Upper part of the hexagon
for i in range(n):
    print(" " * (n - i - 1) + "@" * (n + 2 * i))

# Lower part of the hexagon
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "@" * (n + 2 * i))








