alpha='abcdefghijklmnopqrstuvwxyz'
i=24
print(alpha[i])
print(alpha[i+1])
#print(alpha[i+2]) #Out of Range
print("After %")
print(alpha[(i)%26])    #24
print(alpha[(i+1)%26])  #25
print(alpha[(i+2)%26])  #0

print("shift by 1 lettter")
name="abhishek"
t=""
i=0
#print(name.index("k"))
k=1 #shift a letter by k
t=t+(alpha[(((alpha.index(name[i]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+1]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+4]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+5]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+6]))+k)%26)])
t=t+(alpha[(((alpha.index(name[i+7]))+k)%26)])
print(t)


'''
print(name[i]) # get the variable at i pxn
print(alpha.index(name[i])) #serch for ith variable in alpha and get the pxn
print(alpha.index(name[i])+k) # shifting pxn by k
print(alpha[alpha.index(name[i])+k]) #Shifted variable

'''
#After Week 3

print("Shift by 1 letter")
name = "abhishek"
alpha = "abcdefghijklmnopqrstuvwxyz"
shifted_name = ""
k = 1  # Shift a letter by k

for i in range(len(name)):
    shifted_name += alpha[((alpha.index(name[i]) + k) % 26)]

print(shifted_name)



