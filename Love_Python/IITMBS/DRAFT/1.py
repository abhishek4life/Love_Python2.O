x = int(input())
i = 0
while x % (10 ** i) != x:
    i = i + 1
print(i)

