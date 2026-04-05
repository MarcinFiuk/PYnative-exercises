# Exercise 1: Read a File
# Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
'''
try:
  f = open('sample.txt','r')
  print(f.read())
  f.close()
except FileNotFoundError:
  print('Error, "sample.txt" not found')
'''

# Exercise 2: Read File Line by Line
# Write a Python program to read the text file named “sample.txt” line by line and print each line.
'''
try:
  with open('sample.txt', 'r') as f:
    # for line in f:
    #   print(line)
    # for line in range(3):
    #   print(f.readline())
    content = f.readlines()
    for i in range(len(content)):
      print(content[i])
except FileNotFoundError:
  print('Error, "sample.txt" not found')
'''

# Exercise 3: Read Specific Lines From a File
# Write a Python program to read only the first 5 lines of “sample.txt”.
'''
def read_only_n_lines(n):
  try:
    with open('sample.txt', 'r') as f:
      for i in range(n):
        print(f.readline(), end='')
  except FileNotFoundError:
    print('Error, "sample.txt" not found')

read_only_n_lines(5)
'''

# Exercise 4: Count Words From a File
# Create a function that takes a filename as input and returns the total number of words in that file.
# I have not learn regex
'''
def count_words_in_a_file(file):
  words=0
  try:
    with open(file, 'r') as f:
      content = f.readlines()
      for line in content:
        if ' ' in line:
          words +=len(line.split(' '))
        else:
          words +=1 
    return words
  except FileNotFoundError:
    print('Error, "sample.txt" not found')
  

print(count_words_in_a_file('sample.txt'))
'''

# Exercise 5: Count Total Number of Characters in File
# Write a function that takes a filename as input and returns the total number of characters in that file (including spaces and newlines).

def count_words_in_a_file(file):
  try:
    with open(file, 'r') as f:
      content = f.read()
      return len(content)
  except FileNotFoundError:
    print('Error, "sample.txt" not found')
  

print(count_words_in_a_file('sample.txt'))