r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A=[]
B=[]
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

c=[[0,0,0],[0,0,0],[0,0,0]]

dim=3

#c[i][j] is the dot product of the ith row of A
# and the jth column of B
# c[i][j]= dot product of A[i][....] and B[...][j]


#Old Method
for i in range(dim):
     for j in range(dim):
         for k in range(dim):
             c[i][j]=c[i][j]+A[i][k]*B[k][j]
print(c)

#---------------------------------------------------------------------
import numpy as np
x=np.asmatrix(A)
y=np.asmatrix(B)
print(x*y)
#np.mat` was removed in the NumPy 2.0 release. Use `np.asmatrix` instead.
#I installed (pip install numpy) through terminal
#earlier it was not working


#-----------------------------------------------------------------------
#Using Function


#initialization C to zero
def initialize_mat(dim):
    C=[]
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C

print(initialize_mat(dim))

#Dot Product
def dot_product(u,v):
    dim=len(u)
    ans=0
    for i in range(dim):
        ans=ans+(u[i]*v[i])
    return ans

a=[1,2,3]
b=[4,5,6]
print(dot_product(a,b))

#
def row(A,i):
    dim=len(A)
    l=[]
    for k in range(dim):
        l.append(A[i][k])
    return l

print(row(B,0))

def column(A,i):
    dim=len(A)
    l=[]
    for k in range(dim):
        l.append(A[k][j])
    return l

print(row(A,0))

#Multiplication #Square Matrix
def mat_mul(A,B):
    dim=len(A)
    C=initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j]=dot_product(row(A,i),column(B,j))
    return C

print(mat_mul(A,B))
# some error please fix it



