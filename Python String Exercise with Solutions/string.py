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
'''
s1 = "P@#yn26at^&i5ve"
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
'''

#Exercise 6: Create a mixed String using the following rules
#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
'''
s1 = "Abc"
s2 = "Xyz"
#Expected Output:AzbycX

def special_str(str1,str2):
  str3=""
  str1_len = len(str1)
  str2_len = len(str2)
  length = str1_len if str1_len > str2_len else str2_len
  str2=str2[::-1]

  for i in range(length):
    if i < str1_len:
        str3 = str3 + str1[i]
    if i < str2_len:
        str3 = str3 + str2[i]
  print(str3)

special_str(s1,s2)
'''

#Exercise 7: String characters balance Test

#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
'''
#s1 = "Yn"
#s2 = "PYnative"
s1 = "Ynf"
s2 = "PYnative"

def is_string_in_string(str1,str2):
  index = str2.find(str1)

  print(True if index>=0 else False)

is_string_in_string(s1,s2)
'''

#Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
word = "USA"
'''
def find_all_occurrence(sentence,word):
  
  #occurrence = 0
  #index = 0
  word = word.lower()
  sentence = sentence.lower()
  
  #while index !=-1:
  #  index = sentence.find(word,index+1)
  #  if index !=-1:
  #    occurrence +=1
  occurrence = sentence.count(word)
  print(occurrence)

find_all_occurrence(str1,word)
'''  

#Exercise 9: Calculate the sum and average of the digits present in a string
#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
'''
str1 = "PYnative29@#8496"
def count_average_from_string(str):
  sum=0
  occurrence=0
  for l in str:
    if l.isdigit():
      sum +=int(l)
      occurrence +=1
  average = sum/occurrence
  print(average)

count_average_from_string(str1)
'''

#Exercise 10: Write a program to count occurrences of all characters within a string

str1 = "AppleAppleapple"

def count_occurrence_of_characters(str):
  dic={}
  for l in str:
    if l not in dic:
      count = str.count(l)
      dic[l]=count
  print(dic)

count_occurrence_of_characters(str1)
