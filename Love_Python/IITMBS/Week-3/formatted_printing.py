#output in single line
for i in range(10):
    print(i,end=' ')
print("\nit will print on the same line")
#-----------------------
d=10
m=5
y=2021
print("\nToday date:",d,m,y, sep= '/')
#------------------------
num=int(input("Table of:"))
for i in range (1,11):
    #print(num,"*",i,"=",num*i)
   # print(f'{num}*{i}={num*i}')
    print('{0} * {1} = {2}'.format(num,i,num*i))#print using format funtion
    print('%d*%d=%d' % (num ,i ,num*i))#old way
#------------------------------
pi=22/7
#print(f'Value of PI = {pi}') #3.142857142857143
print(f'Value of PI = {pi:.2f}')#only two digit after fractional part
#print('Value of PI = {0}'.format(pi)) #3.142857142857143
print('Value of PI = {0:.3f}'.format(pi))
#print('value of PI = %f'%(pi))#3.142857
print('value of PI = %.4f'%(pi))
#------------------------------
#left align
print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))
#right align
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))




