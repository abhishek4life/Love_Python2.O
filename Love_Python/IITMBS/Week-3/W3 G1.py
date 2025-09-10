
print("Task:")
print("sum_until_0")
print("total_price")
print("only_ed_or_ing")
print("reverse_sum_palindrome")
print("double_string")
print("odd_char")
print("only_even_squares")
print("only_odd_lines")


# This is the first line of the exercise
task = input("Type Task:")
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input("Type Number To Add:"))
    while n != 0: # the terminal condition
        total += n # add n to the total
        n = int(input("Type Next Number:")) # take the next n form the input
    print(total)



elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input() #Input as Qty price
        if line == "END": # The terminal condition
            break
        quantity, price = line.split() # split uses space by default , split into list
        quantity, price = int(quantity), int(price) # convert to ints
        total_price += quantity * price # accumulate the total price
    print(total_price)


elif task == "only_ed_or_ing":

    word = input("Enter a word (type 'stop' to quit) :")

    while word.lower() != "stop":
        if word.lower().endswith("ed") or word.lower()[-3:]=="ing": # both ways of doing it
            print(word)
        word = input()

elif task == "reverse_sum_palindrome":

    num = int(input())
    while num !=-1:
        rev_num = int(str(num)[::-1])
        num_sum = num+rev_num
        if str(num_sum) == str(num_sum)[::-1]:
            print(num)
        num = int(input())

elif task == "double_string":

    line = input()
    while line != "":
        print(line*2)
        line = input()

elif task == "odd_char":

    line = input()
    while line[-1] != ".":
        print(line[::2],end=" ")
        line = input()
    print(line[::2]) #(which ends with a period) breaks the loop and is processed after the loop by this line.

elif task == "only_even_squares":

    while True:
        line = input()
        if line == "NAN":
            break
        num = int(line)
        if num % 2 == 0:
            print(num * num)

elif task == "only_odd_lines":

    result  = ""
    line_no = 1
    while True:
        line = input()
        if line == "END":
            break
        if line_no%2:
            result = line + "\n" + result
        line_no+=1
    print(result)