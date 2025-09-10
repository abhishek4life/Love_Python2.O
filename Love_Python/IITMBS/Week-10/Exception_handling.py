
# a=int(input())
# b=int(input())
# c=a/b
# print(c)
# f = open('abc.txt', 'r')



a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))
try:
    f = open('abc.txt', 'r')
    c = a / b
    print(f"Result: {c}") #d

except ZeroDivisionError:
    print("Invalid Input, divisor cannot be zero.")
    #pass #use instead
except NameError:
    print('Variable not defined')

except FileNotFoundError:
    print('Invalid File Name , Please Check again')

except: #for all other type of error
    print('Something went wrong')

finally:
    f.close()
    print('from finally block')

#-----------------------------------------
#Creating Own exception
#User defined exception

int(input())
a=int(input())
if a < 18:
    raise Exception( 'You are underage, can not vote')