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





