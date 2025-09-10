# Taking input from the user
n = int(input())

# Generating the pattern
for i in range(n):
    # Printing leading spaces
    print(" " * (n - i - 1), end="")

    # # Printing zeros with space in between
    # print("0 " * (i + 1), end="")
    # Printing zeros with space in between, no trailing space
    print(" ".join(["0"] * (i + 1)))

    # Moving to the next line
    print()
