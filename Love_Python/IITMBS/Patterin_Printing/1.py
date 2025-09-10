n=5

print("Increasing Triangle")
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()

print("Decreasing Triangle")
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()


# We always start printing from left side of the screen
#The number of spaces should decrease for the Right Triangle and
# increase for the Left Triangle as the loop progresses.

print("Right Triangle")
for i in range(n):
    # decreasing space
    # The spaces decrease as i increases, which pushes the stars
    # to the right, forming a Right Triangle.
    for j in range(n-i-1):  #'''(1,n)'''
        print(" ",end=' ') #both spaced
    # increasing Star
    for j in range(i+1):
        print("*",end=' ')
    print()


print("Left Triangle")
for i in range(n):
    # increasing spaces (only one space per iteration)
    for j in range(i): # '''(i+1)'''
        print(" ", end=' ')  # Corrected space
    # decreasing stars
    for j in range(i, n):
        print("*", end=' ')
    print()

#____________________________________
