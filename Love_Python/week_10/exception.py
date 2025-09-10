#Exception Handling

# a=int(input())
# b=int(input())
# c= a/b
# print(c)

#b==0
#ZeroDivisionError: division by zero

#print(d)
#NameError: name 'd' is not defined

#f=open("file.txt","r")
#FileNotFoundError: [Errno 2] No such file or directory: '

#It can be handled using try and except block

a=int(input())
b=int(input())
try:
    c= a/b
    print(c)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
    #pass
except NameError:
    print("Variable not defined")
except:
    print("Some error occured")

#36 Exception there in python

finally:
    f.close()
    print("I will execute anyway")

#CREATING A CUSTOM EXCEPTION
P=INT(input("Enter the percentage"))
if P>100 or P<0:
    raise Exception("Percentage should be between 0 and 100")
    