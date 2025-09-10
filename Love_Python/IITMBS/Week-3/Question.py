x = int(input())
while(x % 5 != 0 and x % 10 != 0):
    x = int(input())
print(x)
#
x = 1
while True:
    expression = x**2 + x + 41
    if expression % 41 == 0:
        print(x)
        break
    x += 1

#
total = 0
for i in range(1, 5):
    for j in range(i):
        total = total + i
print(total)

#
i = 0
while (i < 100):
    print(i * '*')
    i = i + 1

#
for i in range(10):
    for j in range(10):
        break
    break
