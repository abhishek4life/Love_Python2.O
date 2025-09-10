s='VIBGYOR'
for i in range(len(s)):
    print(s[i])

#alternative
for char in s:
    print(char)

#---------------------------
#example for nested for loop
count=0
for i in range(7): #for every i , j very over the range
    for j in range(7):
        #print(s[i],s[j])
        print(i,j,s[i],s[j])
        count=count+1

print("Total way in which the two brother can wear 7 diffrent color:",count)
#----------------------------
#tutorial
#1
print("Prime Number less than entered number")
num= int(input("Enter number:"))
if (num>2):
    print(2,end=' ')#in the same line

for i in range (3,num): # range of outer loop
    flag=False
    for j in range (2,i): #range of inner for loop
        if (i%j==0): #if satisfied then it is not prime number
            flag=False
            break # break inner loop
        else:
            flag=True
    if (flag):
        print(i,end=' ')

#-------------------------------------------------------------------
'''
#2
#find the total profit/loss of each trader working ina trading firm.
# information regarding number of traders and number of transactions is unknown
# input

#SJ_323
#3534 56456 -2432 0                    #output=57558
#-1

empID=input("\nEnter Employee ID:")
while (empID != '-1'):
    trade=int(input("Enter trade amount:"))
    profit_loss=0
    while (trade!=0):
        profit_loss=profit_loss + trade
        trade=int(input("Enter trade amount:"))
    print(f'Profit/loss for employee {empID} is {profit_loss}')
    empID= input('\nEnter employee ID:')
    
'''
#--------------------------------------------------------------------------
#3
'''
Find the day wise total rainfall for the entered duration of time e.g 
week,month,etc.

Day  input                         output 
0     7            
1    10 15 19 5 -1                   49
2    12 13 31 -1                     56
3    57 32 85 47 82 -1               303
4    2 5 8 2 4 8 8 2 -1              39
5    -1                              0
6    21 73 90 3 7 -1                 194
7    30 17 40 10 2 -1                99
'''
days = int(input("\nEnter no. Days:"))
for i in range (1,days+1):
    total=0
    rainfall=int(input("Enter the rainfall:"))
    while(rainfall !=-1):
        total = total + rainfall
        rainfall = int(input("Enter the rainfall:"))
    print('Toatal rainfall for day{0} is {1}'.format(i,total))