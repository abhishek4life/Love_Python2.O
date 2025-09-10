#NumPy:Numerical Python
#ndarray: N-Dimensional array

'''
Parameters                      Python list                         NumPy array
Installation and Importing      Not Required                        Required
Elements                        Hetrogenous                         Homogenous
Dimension Of Element            No Restrication                     Has to be same
Memory allocation               Non contiguous                      Contigous
Sized                           More space                          less space
Performance                     slower                              faster \
Ele wise operation              not possible                        Possible
Functionallity                  can't handle arithmetic             handle
'''

a=[42]
b=[1,2,3,4,5]
c=[[1,2,3],[4,5,6]]
d =[[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]]


print(a,'\n')
print(b,'\n')
print(c,'\n')
print(d,'\n')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import numpy as np
a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])


print(a,a.ndim,'\n')
print(b,b.ndim,'\n')
print(c,c.ndim,'\n')
print(d,d.ndim,'\n')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
