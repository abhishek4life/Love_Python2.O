'''Given an integer n (where n > 0), print an "W" shaped pattern with n rows.

The pattern should consist of a vertical bar (|) on the left and right sides of each row.
Additionally, it should have forward slashes (/) and backslashes ()
moving diagonally towards each other from the top to the bottom.'''


#W
n = int(input("Enter the number of rows: "))
if n > 0:
    for i in range(n):
        print("|", end="")  # Left vertical bar #

        # Forward slash moving diagonally
        print(" " * (n - i - 1) + "/", end="")

        # Backward slash moving toward the center
        print(" " * (2 * i) + "\\", end="")
#

        print(" " * (n - i - 1) + "|")  # Right vertical bar
else:
    pass


#-----------------------------------------------------------
#N
n = int(input("Enter the number of rows: "))
if n > 0:
    for i in range(n):
        print("|", end="")  # Left vertical bar

        print(" " * i + "\\", end="")  # Diagonal line moving right

        print(" " * (n - i - 1) + "|")  # Right vertical bar
else:
    pass

#---------------------------------
#Z
# Input
n = int(input())

# Loop through each row
for i in range(n):
    if i == 0 or i == n - 1:  # Top or bottom row
        print("*" * n)
    else:  # Diagonal rows
        print(" " * (n - i - 1) + "*")



#------------------------------------------------------------
#V
# Input
n = int(input())

# Loop to print the upper rows of the "V"
for i in range(n - 1):
    # Print spaces, backslash (\), spaces, and forward slash (/)
    print(" " * i + "\\" + " " * (2 * (n - i - 1) - 1) + "/")

# Print the bottom row with 'v'
print(" " * (n - 1) + "v")

#----


#X
# Input
n = int(input())

# Top part of the "X"
for i in range(n):
    print(" " * i + "\\" + " " * (2 * (n - i) - 1) + "/")

# Middle part of the "X"
print(" " * n + "x")

# Bottom part of the "X"
for i in range(n - 1, -1, -1):
    print(" " * i + "/" + " " * (2 * (n - i) - 1) + "\\")



