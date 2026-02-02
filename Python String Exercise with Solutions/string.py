#Exercise 1A: Create a string made of the first, middle and last character
#Write a program to create a new string made of an input string’s first, middle, and last character.
'''
def first_middle_last_char():
  initial_string= input("Please provide a string to convert")
  middle_index= int(len(initial_string)/2)
  final_str = initial_string[0]+initial_string[middle_index]+initial_string[-1]
  return final_str

print(first_middle_last_char())
'''

#Exercise 1B: Create a string made of the middle three characters
#Write a program to create a new string made of the middle three characters of an input string.
'''
def three_middle():
    initial_string= input("Please provide a string to convert")
    if len(initial_string)<=3:
      return initial_string
    
    middle_index= int(len(initial_string)/2)
  
    return initial_string[middle_index-1:middle_index+2]

print(three_middle())
'''

#Exercise 2: Append new string in the middle of a given string
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
'''
s1 = "Ault"
s2 = "Kelly"
def append_in_the_middle(str1,str2):
   middle = len(str1)//2
   str3=str1[:2]+str2+str1[2:]
   print(str3)

append_in_the_middle(s1,s2)
'''

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
'''
s1 = "America"
s2 = "Japan"
#expected:AJrpan

def newStr(str1,str2):
  str1mid=len(str1)//2
  str2mid=len(str2)//2
  str3=str1[0]+str2[0]+str1[str1mid]+str2[str2mid]+str1[-1]+str2[-1]
  print(str3)

newStr(s1,s2)
'''

#Exercise 4: Arrange string characters such that lowercase letters should come first
'''
s1 = 'PyNaTive'
def lowercase_letters_first(str1):
  lower=''
  upper=''
  for l in str1:
    if l.islower():
      lower+=l
    else:
      upper+=l

  s2=lower+upper
  print(s2)

lowercase_letters_first(s1)
'''

#Exercise 5: Count all letters, digits, and special symbols from a given string

s1 = "P@#yn26at^&i5ve"
#Expected Outcome:

def count_letters_digits_symbols(str1):
  chars=0
  digits=0
  symbols=0

  for l in str1:
    if l.isalpha():
      chars +=1
    elif l.isdecimal():
      digits +=1
    else:
      symbols +=1
  
  print("Chars =", chars)
  print("Digits =", digits)
  print("Symbols =", symbols)

count_letters_digits_symbols(s1)