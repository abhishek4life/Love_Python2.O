x1 = input("Type X1:")
x2 = input("Type X2:")
y1 = input("Type Y1:")
y2 = input("Type Y2:")
y3 = input("Type Y3:")
z = input("Type Z:")

# swap the values of `x1` and `x2`
x1,x2 = x2,x1

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1
y1,y2,y3 = y2,y3,y1

# create a new variable `a` with the value of `z`
a = z

# delete the variable `z`
del z

print("Output X1:",x1)
print("Output X2:",x2)
print("Output Y1:",y1)
print("Output Y2:",y2)
print("Output Y3:",y3)
print("Output a:",a)