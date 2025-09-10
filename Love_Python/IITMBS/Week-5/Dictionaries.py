'''
Python dictionaries are powerful and versatile data structures that store key-value pairs.
 They are essential for efficient data retrieval and manipulation in many programming tasks.
 Let's explore dictionaries in detail with numerous examples.
'''

#Creating Dictionaries
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

#Using the dict() Constructor
my_dict = dict(name='John', age=30, city='New York')

#with a list of tuples:
my_dict = dict([('name', 'John'), ('age', 30), ('city', 'New York')])

#Dictionary Comprehension
squares = {x: x*x for x in range(5)}
print(squares)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Accessing Values
my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])  # Output: John

#Adding or Modifying Elements
my_dict['job'] = 'Engineer'  # Adding a new key-value pair
my_dict['age'] = 31  # Modifying an existing value

#Removing Elements
del my_dict['job']

#Dictionary Methods
#get()
#The get() method returns the value for a given key, or a default value if the key doesn't exist:
print(my_dict.get('name', 'Not Found'))  # Output: John
print(my_dict.get('salary', 'Not Found'))  # Output: Not Found

#keys(), values(), and items()
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#update()
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

#Iterating Over Dictionaries
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")

#Nested Dictionaries
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}
print(nested_dict['person1']['name'])  # Output: Alice

#Dictionary Comprehension with Conditions
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#Practical Examples
#Counting Word Frequency
text = "the quick brown fox jumps over the lazy dog"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

#Grouping Data
people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'New York'}
]
by_city = {}
for person in people:
    city = person['city']
    by_city.setdefault(city, []).append(person['name'])
print(by_city)
'''setdefault(city, []): Checks if city exists in the by_city dictionary. If not, it adds city with an empty list as its value.
.append(person['name']): Adds the person's name to the list corresponding to the city.'''

#----------------------------------------------------------------------------------------------------
import re

def paragraph_to_word_list(paragraph):
    words = re.findall(r'\b\w+\b', paragraph)
    return words

paragraph = """It was Monday morning. Swaminathan was reluctant to open his eyes.
He considered Monday specially unpleasant in the calendar. After the
delicious freedom of Saturday and Sunday, it was difficult to get into the
Monday mood of work and discipline. He shuddered at the very thought of
school: that dismal yellow building; the fire-eyed Vedanayagam, his class
teacher; and the Head Master with his thin long cane. ... """

word_list = paragraph_to_word_list(paragraph)

#Creating a dictionary with words as keys and initializing counts to 0:
'''d = {}
for x in word_list:
    d[x] = 0
print(d)
'''

# Print each word
print("Each word in the list:")
for x in word_list:
    print(x)

# Create dictionary and initialize counts
d = {}
for x in word_list:
    d[x] = 0

# Count occurrences
for x in word_list:
    d[x] = d[x] + 1
print("\nWord counts:", d)

# Find word with maximum occurrences
max_count = 0
max_word = ''
for word, count in d.items():
    if count > max_count:
        max_count = count
        max_word = word

print("\nMax->", max_word, ":", max_count)



