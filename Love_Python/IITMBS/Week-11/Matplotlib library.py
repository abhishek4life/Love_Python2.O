import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)

x=np.array([6, 9, 12, 11, 4, 9, 2, 17, 2, 7, 8, 7, 5])
y=np.array([80, 79, 72, 88, 81, 97, 109, 82, 82, 81, 81, 80, 93])
plt.scatter(x,y)

#plt.show()

a=np.array(["A","B","C","D"])
b=np.array([3,8,1,10])
plt.bar(a,b)
#plt.barh(a,b) for horizontal bar graph
#plt.show()

#histrograph
v=np.random.normal(170,10,250)
plt.hist(v)
#plt.show()

#piechart
p=np.array([35,25,25,15])
mylabels =["Apple","Banana","Cherries","Dates"]

plt.pie(p,labels=mylabels,startangle=90)
plt.show()