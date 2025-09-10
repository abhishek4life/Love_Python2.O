n=5
print()
print("Hill Pattern")
print()
#Right Triangle
    #Dec Space
    #Inc star
#Increasing star

for i in range(n):
    for j in range(n-i-1):#the space dec as i inc,pushes it to right
        print(" ",end=' ')#both spaced
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i): #peak created by removing 1 column
        print("*",end=' ')
    print()

print()
print("Reverse Hill Pattern")
print()
#Left triangle
    #inc space
    #dec star
#Decreasing star

for i in range(n):
    for j in range(i): #'''(i+1)'''
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    for j in range(n-i-1):
        print('*',end=' ')
    print()


print()
print("Diamond")
print()

#Hill Pattern
for i in range(n-1): #'''(n)''' One less row
    for j in range(n-i-1):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()

#Reverse Hill Pattern

for i in range(n):
    for j in range(i):
        print(" ",end=' ')
    for j in range(i,n):
        print("p",end=' ')
    for j in range(n-i-1):
        print('p',end=' ')

    print()
