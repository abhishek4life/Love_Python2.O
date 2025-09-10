
n=5

#Change In Rows
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p+=1
    print()

print()

p=5
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p-=1
    print()

print()

n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print('A',end='')
        else:
            print('B',end='')
    print()

#---------------------------------

print("\nDiamond Pattern\n")
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")
    p+=1
    print()
p=1
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    p += 1  # Increment `p` so it starts at 1 and reaches 5
    print()


print("\nDiamond Pattern\n")
n = 9

# Hill Pattern (Upper half)
p = 1
for i in range(n - 1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i):
        print(p, end="")
    for j in range(i + 1):
        print(p, end="")
    p += 1
    print()

# Reverse Hill Pattern (Lower half, starting from 1)
p = 1
for i in range(n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i, n - 1):
        print(p, end="")
    for j in range(i, n):
        print(p, end="")
    p += 1  # Increment `p` so it starts at 1 and reaches 9
    print()



#-------------------
print("\nDiamond Pattern\n")
n = 9

# Upper half (Hill Pattern)
for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i + 1):
        print(j + 1, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Lower half (Reverse Hill Pattern)
for i in range(n - 1, 0, -1):
    for j in range(n - i + 1):
        print(" ", end="")
    for j in range(i):
        print(j + 1, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

