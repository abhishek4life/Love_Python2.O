# Find Whether the input number is even or odd

print("Even or Odd")
num=int(input("Typr number to check: "))
if num%2==0:
    print("----------------------------->it is even")
else:
    print("----------------------------->it is not even")


#Find whether the input number is ends with 0 or 5 or any other number


print("Ends with 0,5,Other")
alpha=int(input("Type digit to check: "))
if alpha%5==0:
    if alpha%10==0:
        print("----------------------------->Ends with 0")
    else:
        print("----------------------------->Ends with 5")
else:
    print("-----------------------------> End with Other")
    

#Find the grade of student of based on ythe given marks (0 to 100)

print("Grade")
marks=int(input("Type Your Marks: "))

if (marks>=0 and marks<=100):
    if (marks >=90):
        print('----------------------------->A')
    elif marks>=80 :
        print("----------------------------->B")
    elif marks>=70 :
        print("----------------------------->C")
    elif marks>=60 :
        print("----------------------------->D")
    else:
        print("----------------------------->E")
else:
    print("----------------------------->Invalid Input")
