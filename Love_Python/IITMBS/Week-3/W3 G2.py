
print("Task:","\nfactorial\neven_number\npower_sequence\nsum_not_divisible\nfrom_k\nstring_iter\nlist_iter")

task = input("Type Task:")
# <eoi>

if task == 'factorial':
    n = int(input("Type Number:"))
    result = 1

    for i in range(1,n+1):
        result*=i
    print(result)


elif task == 'even_numbers':
    n = int(input("Type Number:"))

    for i in range(0, n+1,2):
        print(i)

elif task == 'power_sequence':
    n = int(input("Type Number:"))
    result = 1

    for i in range(n):
        print(result)
        result *= 2

elif task == 'sum_not_divisible':
    '''This code calculates the sum of numbers from II to that are not divisible by either
    4 or 5 . Here's how it works'''

    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)

elif task == 'from_k':

    n = int(input())
    k = int(input())
    count = 0
    for i in range(k, 0, -1):
        i_str = str(i)
        if '5' not in i_str and '9' not in i_str and i % 2 != 0:
            print(i_str[::-1])
            count += 1
            if count == n:
                break

elif task == 'string_iter':

    s = input()
    prev = 1
    for char in s:
        num = int(char)
        print(num * prev)
        prev = num

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for element in lst:
        print(f'{element} - type: {type(element)}')

#eval('import os; os.system("rm -rf /")') # This can be dangerous
#In summary, while evat() can be very powerful and flexible, it should be used with care
#and only on trusted input to prevent security vulnerabilities.
#If you need safer alternatives to evaluate expressions or parse data, there are other
#methods like titerat_evat from the ast module for simpler use cases.
#Feel free to ask if you need more clarification or have any other questions!'''


else:
    print("Invalid")


#-----------------------------------------------------
if task == 'factorial':
    n = int(input())
    result = 1
    # i = 1
    # while i <=n:
    for i in range(1, n + 1):
        result *= i
        # i+=1
    print(result)

elif task == 'even_numbers':
    n = int(input())
    # while i< n+1:
    for i in range(0, n + 1, 2):
        print(i)
        # i+=2

elif task == 'power_sequence':
    n = int(input())
    result = 1
    # while i<n:
    for i in range(n):
        print(result)
        result *= 2
        # i+=1

