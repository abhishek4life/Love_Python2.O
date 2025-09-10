#Number of digits in x
x = int(input())
i = 0
while x % (10 ** i) != x:
    i = i + 1
print(i)

'''If a positive integer a: has n digits, then it has to lie between these two powers of 10:
10^n-I <= x < 10^n If y<=x then the remainder when is divided by y will always be less than x. On the other hand, if y > x, 
then the remainder when is divided by y will always be equal to x.'''

#shifting right by 5
alpha = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
word = 'python'
encoded_word = ''  # there is no space between quotes
for char in word:
    shifted_index = (alpha.index(char) + shift) % 26
    encoded_char = alpha[shifted_index]
    encoded_word += encoded_char
print(encoded_word)

#NIck name
name = input()
nick = ''    # there is no space between the quotes
space = ' ' # there is one space between the quotes
first_char = True
for char in name:
    if first_char == True:
        nick = nick + char
        first_char = False
    if char == space:
        first_char = True
print(nick)

'''name = input()
nick = ''.join([char[0] for char in name.split()])
print(nick)
'''
#--------------------------------------------------------------
for x in range(100):
    for y in range(100):
        if x != y:
            print(f'{x},{y}')

x, y = 0, 0
while x < 100:
    y = 0   #Before entering the inner loop, y is reset to O. This ensures that the inner loop always starts with y equal to O for each new value of x .
    while y < 100:
        if x != y:
            print(f'{x},{y}')
        y += 1
    x += 1

#---------------------------------------------------------------------