# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and prints their values.
'''
def print_arg(name,age):
  print('Name: ' +name)
  print('Age: ', +age)

print_arg('Marcin', 99)
'''

# Exercise 2: Create a function with variable length of arguments
# Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
'''
def func1(*args):
  print('Printing values:')
  for arg in args:
    print(arg)
  print()

# call function with 3 arguments
func1(20, 40, 60)
# call function with 2 arguments
func1(80, 100)
'''

# Exercise 3: Return multiple values from a function

# Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.
'''
def calculation(a, b):
    sum = a+b
    difference = a-b
    return sum, difference

res = calculation(40, 10)
print(res)
'''

# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() with the following specifications:
#   It should accept the employee’s name and salary.
#   It should display both the name and salary.
#   If the salary is not provided in the function call, it should default to 9000.
'''
def showEmployee(name, salary=9000):
  print(f'Name: {name}, salary: {salary}')

showEmployee("Ben", 12000)
showEmployee("Jessa")
'''

# Exercise 5: Create an inner function
# Create a program with nested functions to perform an addition calculation as follows:
#   Define an outer function that accepts two parameters, a and b.
#   Inside this outer function, define an inner function that calculates the sum of a and b.
#   he outer function should then add 5 to this sum.
#   Finally, the outer function should return the resulting value.
'''
def outer_func(a,b):
  def inner_func(a,b):
    return a+b
  sum = inner_func(a,b)
  return sum +5 

print(outer_func(3,3))
'''

# Exercise 6: Create a recursive function
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
'''
def sum_range(n):
  if n==0:
    return 0
  else:
    return n + sum_range(n-1)

print(sum_range(10))
'''

# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
'''
def display_student(name, age):
    print(name, age)

show_student = display_student

display_student("Emma", 26)
show_student("Emma", 26)
'''

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
'''
def generate_even_numbers_from_range(start,stop):
    print(list(range(start,stop,2)))

generate_even_numbers_from_range(4,30)
'''

# Exercise 9: Find the largest item from list
'''
l1 = [4, 6, 8, 24, 12, 2]

def find_max(list):
  print(max(list))

find_max(l1)
'''

# Exercise 10: Call Function using both positional and keyword arguments
# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function using both positional and keyword arguments.

def describe_pet(animal_type, pet_name):
  print(animal_type, pet_name)

describe_pet('dog', 'Bingo')
describe_pet(animal_type='dog',pet_name='Bingo')