'''
Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month,
 fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number)
  separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")


Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called
as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.

Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".
Note: Finding the tenth_month will be a bit of challange. If you are stuck open the below hint.

Hint for tenth_month
Problem Type: Standard Input - Standard Output
'''

age = int(input("Type Your Age:")) # int: Read a number as integer from standard input
dob = input("dob dd/mm/yy:") # str: Read a string of format dd/mm/yy from standard input
day, month, year =...  # int, int, int: Get the correct parts from dob as int
print(day,month,year)

fifth_birthday =... # str: fifth birthday formatted as day/month/year
print("5th Birthday:",fifth_birthday)

last_birthday =... # str: last birthday formatted as day/month/year
print("Last Birthday:",last_birthday)

month += 10
month, year =...
tenth_month =... # str: dob same day after 10 months formatted as day/month/year

... # print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space


weight =... # float: Read a number as float from stdin(Standard input)

kg =...  # Get the integer part (kg)
grams =...  # Get the fractional part converted to grams

weight_readable =... # str: reformat weight of format 55 kg 250 grams

# print weight_readable
print(weight_readable)

#--------------------------------------------------------------------------------

