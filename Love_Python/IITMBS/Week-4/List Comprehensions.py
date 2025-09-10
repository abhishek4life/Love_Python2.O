a=10
b=20
'''
if a<b:
    small=a
else:
    small=b
print(small)'''


small= a if a<b else b
print(small)
'''
x=5
while a>0:
    a-=1'''
x=5
while a>0: print(a); a-=1

#list comprehension
fruits =["mango","apple","banana","orange","pineapple","watermelon","guava","kiwi"]
'''
newlist=[]
for fruit in fruits:
    if 'n' in fruit:
        newlist.append(fruit.capitalize())
print(newlist)'''

newlist = [fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newlist)
