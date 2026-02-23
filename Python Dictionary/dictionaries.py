# Exercise 1: Perform basic dictionary operations
# Perform following operations on given dictionary
#   Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
#   Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
#   Access Key: Print the value associated with the city key.
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print('Original dictionary:', my_dict)
my_dict['profession'] = 'Doctor'
my_dict.update({'age':40})
print('Updated dic:', my_dict)
print(f'City: {my_dict['city']}')
'''

# Exercise 2: Perform dictionary operations
# Perform following operations on given dictionary
#   Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
#   Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
#   Check if Key Exists in the dictionary
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

print('Original dictionary:', my_dict)
my_dict.pop('profession')
print('Updated dictionary after removing \'profession\':', my_dict)
print('Printing all key-value pairs:')
for key,value in my_dict.items():
  print(f'{key} : {value}')
print('Does \'age\' exist?', 'age' in my_dict)
'''

# Exercise 3: Dictionary from Lists
# Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def create_dic(l1,l2):
  # new_dic={}
  # for key,val in zip(l1,l2):
  #   new_dic[key] = val
  new_dic = dict(zip(l1,l2))
  print(new_dic)

create_dic(keys,values)
'''

# Exercise 4: Clear Dictionary
# Clear all key-value pairs from a given dictionary and print it.
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print('Original dictionary:', my_dict)
my_dict.clear()
print('Empty dictionary', my_dict)
'''

# Exercise 5: Merge two Python dictionaries into one
# Write a code to merge two dictionaries into a new dictionary and print it.
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
new_dic = {**dict1, **dict2}
print('New dictionary: ',new_dic)
'''

# Exercise 6: Count Character Frequencies
# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
'''
string1 = 'Jessa'

def check_frequencies(word):
  letter_frequencies= {}
  # for char in word:
  #   if char in letter_frequencies:
  #     letter_frequencies[char] = letter_frequencies[char]+1
  #   else:
  #     letter_frequencies[char] =1

  # Second solution
  for char in word:
    # Use get() method: if char is in dict, get its value; otherwise, default to 0
  #   letter_frequencies[char] = letter_frequencies.get(char, 0) + 1
  # print(letter_frequencies)

check_frequencies(string1)
'''

# Exercise 7: Access Nested Dictionary
# Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.
'''
data = {'person': {'name': 'Alice', 'age': 30}}
print(data['person']['age'])
'''

# Exercise 8: Print the value of key ‘history’ from nested dict
'''
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]['student']['marks']['history'])
'''

# Exercise 9: Modify Nested Dictionary
# In the below dictionary, change name to ‘Jessa’.
'''
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict["class"]['student']['name'] = "Jessa"
print(nested_student_dict)
'''

# Exercise 10: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.
'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dic = {}

for i in range(len(employees)):
  new_dic.setdefault(employees[i],defaults)

print(new_dic)

new_dic1 = dict.fromkeys(employees,defaults)
print(new_dic1)
'''

# Exercise 11: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dic = {k:sample_dict[k] for k in keys}
print(new_dic)
'''

# Exercise 12: Delete a list of keys from a dictionary
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for el in keys:
    del sample_dict[el]

print(sample_dict)
'''

# Exercise 13: Check if a value exists in a dictionary
# While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.
# Write a Python program to check if the value 200 is present in the provided dictionary.
'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}

def check_if_val_exist(dictionary,value):
    if value in dictionary.values():
        print(f'{value} is present in the dictionary')
    else:
        print(f'{value} is NOT present in the dictionary')

check_if_val_exist(sample_dict,200)
'''

# Exercise 14: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
'''
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
'''

# Exercise 15: Get the key of a minimum value
# Write a code to print the key of a minimum value from the following dictionary.
'''
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_val = min(sample_dict)
print(min_val)
'''

# Exercise 16: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
'''
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500

print(sample_dict)
'''

# Exercise 17: Invert Dictionary
# Write a code to swap keys and values in a dictionary. Assume all values are unique
'''
# Inverted dictionary 1: {1: 'a', 2: 'b', 3: 'c'}
original_dictionary= {'a': 1, 'b': 2, 'c': 3}
inverted_dictionary = {val:key for key, val in original_dictionary.items()}

print(f"Original dictionary: {original_dictionary}")
print(f"Inverted dictionary: {inverted_dictionary}")
'''

# Exercise 18: Sort Dictionary by Keys
# Sort a dictionary by its keys and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
'''
my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

sorted_dic_1 = dict(sorted(my_dict.items()))
print(sorted_dic_1)
sorted_dic_2 = sorted(my_dict.items())
print(sorted_dic_2)

from collections import OrderedDict

sorted_dic_3 = OrderedDict(sorted(my_dict.items()))
print(sorted_dic_3)
'''

# Exercise 19: Sort Dictionary by Values
# Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
'''
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}

sorted_dict_1 = dict(sorted(my_dict.items(), key=lambda el:el[1]))
print(sorted_dict_1)
'''

# Exercise 20: Check if All Values are Unique
# Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.

dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {} # Empty dictionary (all values are vacuously unique)

def is_unique(el):
  set_1 = set(list(el.values()))
  print(set_1, el)
  if len(set_1) == len(el):
    print(f'Dictionary: {el} -> All values unique?\n Yes')
  else:
    print(f'Dictionary: {el} -> All values unique?\n No')

is_unique(dict1)
is_unique(dict2)
is_unique(dict3)