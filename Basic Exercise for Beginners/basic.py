# Exercise 1: Calculate the multiplication and sum of two numbers 
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''
num1=20
num2=30
num1=40
num2=30

def multiplication_or_sum(n1,n2):
  if n1*n2<=1000:
    return n1*n2
  return n1+n2

print(multiplication_or_sum(num1,num2))
'''

#Exercise 2: Print the Sum of a Current Number and a Previous number
#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
'''
def print_sum_and_prev(num):
  for n in range(num):
    prev = 0 if n-1<0 else n-1  
    sum = n+prev
    print(f"Current Number {n} Previous Number  {prev}  Sum:  {sum}")

print_sum_and_prev(10)
'''

#Exercise 3: Print characters present at an even index number
#Write a Python code to accept a string from the user and display characters present at an even index number.
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
'''
def print_only_even_index():
  str=input("please provide a string ")
  print("Orginal String is", str)
  print("Printing only even index chars")

  length = len(str)

  for i in range(0,length-1,2):
   print(f"Index: {i}, word: {str[i]}")


print_only_even_index()
'''

#Exercise 4: Remove first n characters from a string
#Write a Python code to remove characters from a string from 0 to n and return a new string.
'''
def remove_chars(word, n):
  word_size = len(word)

  if n>=word_size:
    return "To many characters to remove"
  
  print("Removing characters from a string")
  new_word = word[n:]
  return new_word

print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed
print(remove_chars("pynative", 2)) 
# output 'native'
'''

#Exercise 5: Check if the first and last numbers of a list are the same
#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
'''
numbers = [10, 20, 30, 40, 10]
#numbers = [75, 65, 35, 75, 30]

def is_first_and_last_identical(list):
  is_identical = True if list[0] == list[len(list)-1] else False
  return is_identical

print(is_first_and_last_identical(numbers))
'''

#Exercise 6: Display numbers divisible by 5
#Write a Python code to display numbers from a list divisible by 5
'''
list=[10, 20, 33, 46, 55]

def is_divisible_by_nr(list,divisor):
  for nr in list:
    if nr%divisor==0:
      print(nr)

is_divisible_by_nr(list,5)
'''

#Exercise 7: Find the number of occurrences of a substring in a string
#Write a Python code to find how often the substring “Emma” appears in the given string.
'''
str_example = "Emma is good developer. Emma is a writer"
sub_str = "Emma"

def find_str_occurrences(str,word):
  return str.count(word)

print(find_str_occurrences(str_example,sub_str))
'''

#Exercise 8: Print the following pattern:
#1
#22
#333
#4444
#55555

#def print_pattern(nr_of_rep):
'''
  for n in range(1,nr_of_rep+1):
    occurrence=0
    line=""
    while occurrence<n:
      line +=str(n)
      occurrence+=1
    print(line)
'''
'''
  for num in range(nr_of_rep+1):
    for i in range(num):
        print (num,end=' ') 
    print("\n")
'''
#print_pattern(8)

#Exercise 9: Check Palindrome Number
#Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
'''
def check_palindrome(num):

  print("original number", num)
  if str(num)==str(num)[::-1]:
    print("Yes. given number is palindrome number")
  else:
    print("No. given number is not palindrome number")

check_palindrome(4544)
'''

#Exercise 10: Merge two lists using the following condition
#Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def special_list_combine(l1,l2):
  newList=[]
  for el in l1:
    if el%2!=0:
      newList.append(el)
  for el in l2:
    if el%2==0:
      newList.append(el)clear
  return newList

print(special_list_combine(list1, list2))
'''

#Exercise 11: Get each digit from a number in the reverse order.
#For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
'''
number = 7536

def digit_in_reverse_order(n):
  print("Starting number", n)
  result=""
  while n>0:
    last_dig = n % 10
    result+=str(last_dig)
    n = n//10
    if n!=10:
      result+=" "
  return result

print(digit_in_reverse_order(number))
'''

#Exercise 12: Calculate income tax
#Calculate income tax for the given income by adhering to the rules below
#Taxable Income	|Rate (in %)
#First $10,000	|0
#Next $10,000	  |10
#The remaining	|20
'''
def calculate_income_tax(income):
  tax=0

  if income<=10000:
    tax = 0
  elif income <=20000:
    rest = income - 10000
    tax = rest*0.1
  else:
    rest = income-20000
    tax = 10000*0.1 + rest*0.2
  
  return tax

print(calculate_income_tax(45000))
'''  

#Exercise 13: Print multiplication table from 1 to 10
#The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
#Write a code to generates a complete multiplication table for numbers 1 through 10.
'''
def print_multiplication_table():
  for el in range(1,11):
    for internal_el in range(1,11):
      print(internal_el*el, end=" ")
    print("\t")

print_multiplication_table()
'''

#Exercise 14: Print a downward half-pyramid pattern of stars
'''
def print_downwards_half_pyramid(size):
  for el in range(size,0,-1):
    for internal_el in range(1,el+1):
      print("*",end=" ")
    print('\t')

print_downwards_half_pyramid(5)
'''

#Exercise 15: Get an int value of base raises to the power of exponent
#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
#Note here exp is a non-negative integer, and the base is an integer.
'''
def pow(base,exponent):

  if base <0 or exponent<0:
    return "value must to be bigger than 0"

  res = 1
  for _ in range(1,exponent+1):
    res *=base
  print(res)

pow(5,4)
'''

#Exercise 16: Check Palindrome Number
#Write a code to check if given number is palindrome.
'''
Ex 9 is the same
'''

#Exercise 17: Generate Fibonacci series up to 15 terms
'''
def generate_Fibonacci_series(n):
  fibonacci_list=[0,1]
  
  for i in range(1,n-1):
    print(i)
    fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i])

  return fibonacci_list

print(generate_Fibonacci_series(15))
'''

#Exercise 18: Check if a given year is a leap year
#Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
'''
year1 = 2020 # Output True
year2 = 2025 # Output False

def check_if_leap_year(year):
  if year%4==0 and (year%100 !=0 or year%400 ==0):
    return True
  return False

print(check_if_leap_year(400))
'''

#Exercise: 19: Print Alternate Prime Numbers till 20
'''
def check_if_is_prime(num):
  if num<=1:
    return False
  
  for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        return False
    
  return True

def get_all_prime_till(n):
  prime_list=[]
  for el in range(2,n+1):
    if check_if_is_prime(el):
        prime_list.append(el)
  return prime_list

def get_alternate(list):
  alternate =list[::2]
  return alternate

print(get_all_prime_till(20))
print(get_alternate(get_all_prime_till(20)))
'''

#Exercise 20: Print Reverse Number Pattern
#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
#5 
'''
def print_reverse_number_pattern(n):
  max_range = n+1
  for i in range(1,max_range):
    for j in range(0,max_range-i):
      print(i,end=" ")
    print()

print_reverse_number_pattern(5)
'''

#Exercise 21: Check if a user-entered string contains any digits using a for loop
'''
str1="Pynative123Python"
str2="PYnative"

def contains_digits(phrase):
  for i in range(len(phrase)):
    if phrase[i].isnumeric():
      print("The string contains at least one digit.")
      return
  print("The string does not contain any digits.")

contains_digits(str1)
'''

#Exercise 22: Capitalize the first letter of each word in a string
'''
str1 = "pynative.com is for python lovers"
def capitalize_first_letter_of_each_word(str):
  list = str.split(" ")
  capitalize_list = [word.capitalize() for word in list]
  new_str = " ".join(capitalize_list)
  return new_str

print(capitalize_first_letter_of_each_word(str1))
'''

#Exercise 23: Create a simple countdown timer using a while loop.
'''
import time 

def countdown(sec):
  while sec>0:
    print(f"Time remaining: {sec} seconds")
    time.sleep(1)
    sec -=1
  print("Time's up!")

countdown(5)
'''
