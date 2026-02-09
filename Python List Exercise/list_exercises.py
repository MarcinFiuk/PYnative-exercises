# Exercise 1: Perform Basic List Operations
# Perform following operations on given list
# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.
my_list = [10, 20, 30, 40, 50]
'''
def check_operations(l):
  print(f'Third item: {l[2]}')
  print(f'Length of the list: {len(l)}')
  if len(l)==0:
    print('The list is empty')
  else:
    print('The list is not empty')

check_operations(my_list)
'''

# Exercise 2: Perform List Manipulation
# Perform following list manipulation operations on given list
# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.
'''
def list_manipulation(l):
  print(f'Initial list: {l}')
  l[1]=200
  print(f'List after changing second value: {l}')
  l.append(600)
  print(f'List after appending value: {l}')
  l.insert(2,300)
  print(f'List after inserting value to index 2: {l}')
  l.remove(600)
  print(f'List after removing 600: {l}')
  l.pop(0)
  print(f'list after removing element at index 0: {l}')

list_manipulation(my_list)
'''

# Exercise 3: Sum and average of all numbers in a list
'''
def sum_and_average_list_elements(l):
  List_sum = sum(l)
  list_len =len(l)
  average = List_sum/list_len

  print(f'Sum: {List_sum}')
  print(f'Average: {average}')

sum_and_average_list_elements(my_list)
'''

# Exercise 4: Reverse a list
'''
list1 = [100, 200, 300, 400, 500]

def reverse_list(l):
  print(f'Initial list {l}')
  # l.reverse()
  # print(f'Reversed list {l}')
  reversed_list = l[::-1]
  print(f'Reversed list {reversed_list}')

reverse_list(list1)
'''

# Exercise 5: Turn every item of a list into its square
'''
numbers = [1, 2, 3, 4, 5, 6, 7]

def get_square(l):
  for i in range(len(l)):
    l[i] = l[i]*l[i]
  print(l)

get_square(numbers)
'''

# Exercise 6: Find Maximum and Minimum
'''
data = [8, 2, 15, 1, 9]

def find_max_and_min(l):
  max_val = max(l)
  min_val = min(l)
  print(f'Largest number: {max_val}')
  print(f'Smallest number: {min_val}')

find_max_and_min(data)
'''

# Exercise 7: Count Occurrences
# Count and print how many times 'Football' appears in list.
'''
sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']

def find_occurrence(l,word):
  occurrence = l.count(word)
  print(f'Word {word} appeared {occurrence} times')
  
find_occurrence(sports,"Football")
'''

# Exercise 8: Sort a list of numbers
'''
numbers = [5, 2, 8, 1, 9]

def sort_list_ascending(l):
  print(f'Original list: {l}')
  # l.sort()
  # print(f'Sorted list {l}')
  new_list = sorted(l)
  print(f'Sorted list: {new_list}')

sort_list_ascending(numbers)
'''

# Exercise 9: Create a copy of a list
'''
l1= [10, 20, 30]

def create_copy(l):
  new_list = l.copy()
  l.append(40)
  print(f'list A: {l}')
  print(f'list B: {new_list}')

create_copy(l1)
'''

# Exercise 10: Combine two lists
'''
list_a = [1, 2]
list_b = [3, 4]

def combine_two_lists(l1,l2):
  new_list_A = l1+l2
  l1.extend(l2)
  print(f'combined list: {new_list_A}')
  print(f'combined list: {l1}')

combine_two_lists(list_a,list_b)
'''

# Exercise 11: Remove empty strings from the list of strings
'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

def remove_empty_elements(l):
  filtered_list = filter(None, l)
  print(list(filtered_list))

remove_empty_elements(list1)
'''

# Exercise 12: Remove Duplicates from list
'''
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

def remove_duplicates(l):
  new_list = list(set(l))
  print(new_list)

remove_duplicates(list_with_duplicates)
'''

# Exercise 13: Remove all occurrences of a specific item from a list
'''
list1 = [5, 20, 15, 20, 25, 50, 20]

def remove_all_occurrence_of_element(l,el):

  while el in l:
    l.remove(20)

  print(l)

remove_all_occurrence_of_element(list1,20)
'''

# Exercise 14: List Comprehension for Numbers
# Use list comprehension to create a new list containing only the numbers from a given list.
'''
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

def extract_numbers(l):
  new_list = [el for el in l if isinstance(el, (int,float))]
  print(new_list)

extract_numbers(my_list)
'''

# Exercise 15: Access Nested Lists
# Given a nested list, print the element '55'.

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

print(nested_list[1][1])
