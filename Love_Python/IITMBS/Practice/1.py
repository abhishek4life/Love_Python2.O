print("Odd Diamond")
n=5
p="*"
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")

    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    print()
#---------------------------------
print("Obtuse Triangle")

def obtuse_triangle(Theta1, Theta2):
    a = Theta1
    b = Theta2
    c = 180 - (a + b)

    if max(a, b, c) > 90:
        return True
    else:
        return False

print(obtuse_triangle(100, 40))  # Output: True
print(obtuse_triangle(60, 60))   # Output: False

#--------------------------------
print("Average")
def average_of_repeated_values():
    values = []

    while True:
        user_input = input("Enter a value: ")

        if user_input == 'End':
            break
        elif user_input == 'NoN':
            continue
        else:
            try:
                values.append(float(user_input))
                average = round(sum(values) / len(values), 1)
                print(f"Current average: {average}")
            except ValueError:
                print("Invalid input. Please enter a number, 'NoN', or 'END'.")

    if values:
        final_average = sum(values) / len(values)
        return final_average
    else:
        return None

print(average_of_repeated_values())

#--------------------------------------------------
def remove_elements_from_tuple(tpl, i, n):
    # Ensure the index and number of elements to remove are within valid range
    if i < 0 or i >= len(tpl) or n <= 0:
        return tpl
    # Split the tuple into three parts and reassemble without the specified elements
    new_tpl = tpl[:i] + tpl[i+n:]
    return new_tpl


my_tuple = (1, 2, 3, 4, 5, 6, 7)
index = 2
num_elements = 3
result = remove_elements_from_tuple(my_tuple, index, num_elements)
print(result)  # Output will be (1, 2, 6, 7)

#-------------------------------------------------
def markdown_to_html_image(markdown_text):
    result = markdown_text
    while '![' in result and '](' in result:
        start = result.find('![')
        alt_start = start + 2
        alt_end = result.find(']', alt_start)
        url_start = result.find('(', alt_end) + 1
        url_end = result.find(')', url_start)
        alt_text = result[alt_start:alt_end]
        image_url = result[url_start:url_end]
        html_image = f'<img src="{image_url}" alt="{alt_text}">'
        result = result[:start] + html_image + result[url_end + 1:]
    return result

# Example usage
markdown_text = "![Sample Image](https://example.com/image.jpg)"
html_text = markdown_to_html_image(markdown_text)
print(html_text)

#-----------------------------------------------------------------
def first_non_repeating_character(string):
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            return string[i]
    return None

# Test the function
string = "swiss"
result = first_non_repeating_character(string)

if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating characters found.")

#-----------------------------------------------------------------
#one more question

