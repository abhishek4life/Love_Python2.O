#Change in column
#Managed By Innner Loop


#Increasing Triangle
n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()

#Hill triangle
n=5
for i in range(n):
    p=1
    for j in range(n-i-1):
        print(" ",end=' ')
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    for j in range(i):
        print(p,end=' ')
        p+=1
    print()



print("L Shaped")
print()
n = 5
k = 5

for i in range(n):
    p = k
    for j in range(i + 1):
        print(p, end=" ")
    for j in range(i, n - 1):  # Corrected loop to ensure proper spacing
        print(p, end=" ")
        p -= 1  # Decrease p for descending order
    k -= 1  # Decrease k for the next row
    print()



for i in range(n):
    p=1
    for j in range(n-i-1):#the space dec as i inc,pushes it to right
        print(" ",end=' ')#both spaced
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    for j in range(i): #peak created by removing 1 column
        print(p,end=' ')
        p-=1
    print()


print("\n Floyd Triangle")

n=4
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end='')
        p+=1
    print()