for i in range(2):
    print(i,"Hello World")
    print("****************")

#--------------------------------------
n=int(input("Enter a number:"))
for i in range(n):
    if(i%2==0):
        print(i,"Hello") #even no
    else:
        print(i,"hi") #odd no
#---------------------------------------
#add the first n number
print("Add first n number")
n=int(input("Enter a number to add:"))
ans=0
for i in range (n):
    ans=ans+i
print("the answer is :",ans)

#------------------------------------------
#for multiplication table
print("Table")
for i in range(1,11):
    print("2*",i,"=",2*i)
#------------------------------------------
for i in range(1,11,2):
    print(i)
#-------------
#for loop without range
country="India"
for letter in country:
    print(letter)
#-------------
for i in range(1,11):
    print(i)

i=1 #initialization
while i in range(1,11):
    print(i)
    i +=1 #you have to increment otherwise in loop

#-------------------------------------------------


