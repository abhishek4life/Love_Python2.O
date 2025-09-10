n = int(input())

for i in range(n - 1):
    print(" " * i + "\\" + " " * (2 * (n - 1 - i) - 1) + "/", end=" ")
    print()
print(" " * (n - 1) + "v")
