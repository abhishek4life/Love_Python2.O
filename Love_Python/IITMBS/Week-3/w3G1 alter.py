task = input("Type Task:")

if task == "sum_until_0":
    total = 0
    print("Type Digit To Add:")

    while True:
        n = int(input())  # take the next number from the input
        if n == 0:        # the terminal condition
            break         # exit the loop if n is 0
        total += n        # add n to the total

    print(total)

elif task == "only_ed_or_ing":
    while True:
        word= input()
        if word.lower() == "stop":
            break
        if word.lower().endswith("ed") or word.lower().endswith("ing"):
            print(word)

elif task == "reverse_sum_palindrome":

    # Read an integer input from the user
    num = int(input())

    # Continue the loop until the user enters -1
    while num != -1:
        # Reverse the digits of the number by converting it to a string, reversing it, and converting it back to an integer
        rev_num = int(str(num)[::-1])

        # Calculate the sum of the number and its reverse
        num_sum = num + rev_num

        # Check if the sum is a palindrome by comparing the sum with its reverse (as strings)
        if str(num_sum) == str(num_sum)[::-1]:
            # If the sum is a palindrome, print the original number
            print(num)

        # Read the next integer input from the user
        num = int(input())
elif task == "odd_char":
    while True:
        line = input()
        if line[-1] !=".":
            break
        print(line[::2])

elif task == "only_odd_lines":
    result  = []
    line_no = 1
    while True:
        line = input()
        if line == "END":
            break
        if line_no % 2 != 0:
            result.append(line)
        line_no += 1
    print("\n".join(result[::-1]))
