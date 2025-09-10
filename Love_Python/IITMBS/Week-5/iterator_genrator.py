#Functional Programming

fruits=["mango","apple","orange","pineapple","watermelon","guava","kiwi"]
for fruit in fruits:
    print(fruit) #list,tuple,string etc is iterable

#iterator
'''Iterators are objects that allow you to go through a collection of items one by one. 
They're useful when you want to process data sequentially without loading everything into memory at once'''
basket=iter(fruits)
print(basket)#iterator(type)
print(next(basket))
print(next(basket))
print(next(basket))

#Gererator
'''
Generators are a special type of function that returns an iterator. They use the yield keyword to produce values one 
at a time, which is great for working with large datasets or creating sequences efficiently.
'''
def square(limit):
    x=0
    while x < limit:
        yield x*x
        yield x*x*x
        x=+1

a = square(10)
try:
    print(next(a), next(a))
    print(next(a), next(a))
    print(next(a), next(a))
except StopIteration:
    print("No more values to yield.")


