#Exercise 1: Print first 10 natural numbers using while loop
'''
def print_with_while_loop(n):
  num = 1
  while num<=n:
    print(num)
    num +=1

print_with_while_loop(10)
'''

#Exercise 2: Print the following pattern
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5
'''
def print_pattern(num):
  for i in range(num +1):
    for j in range(1, i+1):
      print(j, end=" ")
    print("")

print_pattern(10)
'''

#Exercise 3: Calculate sum of all numbers from 1 to a given number
'''
def sum_all_numbers_till(num):
  sum=0
  for n in range(1,num+1):
    sum+=n
  return sum

print(sum_all_numbers_till(10))
'''

#Exercise 4: Print multiplication table of a given number
'''
def multiplication_table(num):
  print(f'multiplication for number: {num}')
  for i in range(1,11):
    print(f'{i}X{num}={i*num}')

multiplication_table(2)
'''

#Exercise 5: Display numbers from a list using a loop
#Write a Python program to display only those numbers from a list that satisfy the following conditions
#-The number must be divisible by five
#-If the number is greater than 150, then skip it and move to the following number
#-If the number is greater than 500, then stop the loop
'''
numbers = [12, 75, 150, 180, 145, 525, 50]

def display_special_numbers(list):
  for n in list:
    if n >500:
      break
    if n>150:
      continue
    if n%5==0:
      print(n)

display_special_numbers(numbers)
'''

#Exercise 6: Count the total number of digits in a number
#Write a Python program to count the total number of digits in a number using a while loop.
'''
number = 758697
def count_digits_in_a_number(num):
  nr_of_digits = 0
  while num>0:
    nr_of_digits+=1
    num //=10
  return nr_of_digits

print(count_digits_in_a_number(number))
'''

#Exercise 7: Print the following pattern
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1
'''
def print_pattern(n):
  for i in range(n,0,-1):
    for j in range(i,0,-1):
      print(j,end=" ")
    print()

print_pattern(8)
'''

#Exercise 8: Print list in reverse order using a loop
'''
list1 = [10, 20, 30, 40, 50]
def print_lint_reverse(list):
  #for el in list[::-1]:
  for el in reversed(list):
    print(el)

print_lint_reverse(list1)
'''

#Exercise 9: Display numbers from -10 to -1 using for loop
'''
def display_negative_num(start, end):
  for n in range(start,end+1,1):
    print(n)

display_negative_num(-10,-1)
'''

#Exercise 10: Display a message “Done” after the successful execution of the for loop
'''
def print_message_after_loop(msg):
  for i in range(5):
    print(i)
  else:
    print(msg)

print_message_after_loop("Done")
'''

#Exercise 11: Print all prime numbers within a range
'''
def print_primes(start,end):
  print(f"Prime numbers between {start} and {end} are:")
  for num in range(start,end+1):
    if num<=1:
      continue
    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        break
    else:
        print(num)

print_primes(25,50)
'''

#Exercise 12: Display Fibonacci series up to 10 terms
'''
def display_Fibonacci(num):
  num1=0
  num2=1
  for n in range(1,num+1):
    print(num1,end=" ")
    result=num1+num2
    num1=num2
    num2=result

display_Fibonacci(10)
'''

#Exercise 13: Find the factorial of a given number
'''
def count_factorial(num):
  result=1

  for n in range(2,num+1):
    result *=n

  return result

print(count_factorial(5))
'''

#Exercise 14: Reverse a integer number
'''
def reverse_int(num):
  reverse=0
  while num>0:
    digit = num%10
    reverse =reverse*10+digit
    num = num//10
  
  print(reverse)

reverse_int(76543)
'''

#Exercise 15: Print elements from a given list present at odd index positions
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def print_odd_index_numbers(list):
  for el in list[1::2]:
    print(el, end=" ")


print_odd_index_numbers(my_list)
'''

#Exercise 16: Calculate the cube of all numbers from 1 to a given number

#Write a Python program to print the cube of all numbers from 1 to a given number
'''
import math
input_number = 6

def print_all_cubes(n):
  for num in range(1,n+1):
    print(f"Current Number is : {num}  and the cube is {math.pow(num,3)}")

print_all_cubes(input_number)
'''

#Exercise 17: Find the sum of a series of a number up to n terms
#Write a program to calculate the sum of this series up to n terms. For example, if the number is 2 and the number of terms is 5, then the series will be 2+22+222+2222+22222=2469
'''
num = 2
terms = 5

def sum_of_series(n,terms):
  sum=0
  number=n
  for i in range(terms):
    sum+=number
    number=number*10+n
  
  return sum

print(sum_of_series(num,terms))
'''

#Exercise 18: Print the following pattern
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*
'''
def print_pattern(deep_lv):
  for i in range(deep_lv*2):
    if i<=deep_lv:
      level = i
    else:
      level = deep_lv - (i-deep_lv)
    for j in range(level):
      print("*", end=" ")
    print()

print_pattern(5)
'''

#Exercise 19: Print Full Multiplication Table
#The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
'''
def print_multiplication_table(num):
  for i in range(1,num+1):
    print(f"multiplication table of: {i}")
    for j in range (1,11):
      print(j*i, end=" ")
    print()

print_multiplication_table(10)
'''

#Exercise 20: Print the alternate numbers pattern
#1  
#2 3  
#4 5 6  
#7 8 9 10  
#11 12 13 14 15

def print_pattern(lvl):
  starting_nr=0
  for i in range(1,lvl+1):
    for j in range (0,i):
      starting_nr +=+1
      print(starting_nr, end=" ")
    print()

print_pattern(5)
