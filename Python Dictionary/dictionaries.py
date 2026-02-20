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

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
new_dic = {**dict1, **dict2}
print('New dictionary: ',new_dic)