spam = "That is Alice's cat."

spam = 'Say hi to Bob\'s mother.'

# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

print("Hello there!\nHow are you?\nI\'m doing fine.")
# Hello there!
# How are you?
# I'm doing fine.

print(r'The file is in C:\Users\Alice\Desktop')
# The file is in C:\Users\Alice\Desktop

print('Hello...\n\n...world!')  # Without a raw string
#Hello...

#...world!

print(r'Hello...\n\n...world!')  # With a raw string
# Hello...\n\n...world!

print('''Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob''')

# Dear Alice,

# Can you feed Eve's cat this weekend?

# Sincerely,
# Bob

print("Dear Alice,\n\nCan you feed Eve's cat this weekend?\n\nSincerely,\nBob")
# This print() call prints identical text but doesn’t use a multiline string.

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def say_hello():
    """This function prints hello.
    It does not return anything."""
    print('Hello!')


# '   H  e   l   l   o  ,     w  o  r  l  d   !  '
#     0  1   2   3   4  5  6  7  8  9 10  11 12
#   -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1

greeting = 'Hello, world!'
greeting[0]
'H'
greeting [4]
'o'
greeting[-1]
'!'
greeting[0:5]
'Hello'
greeting[:5]
'Hello'
greeting[7:-1]
'world'
greeting[7:]
'world!'

greeting = 'Hello, world!'
greeting_slice = greeting[0:5]
greeting_slice
'Hello'
greeting
'Hello, world!'
# slicing a string doesn’t modify the original string

'Hello' in 'Hello, World'
True
'Hello' in 'Hello'
True
'HELLO' in 'Hello, World'
False
'' in 'spam'
True
'cats' not in 'cats and dogs'
False

name = 'Al'
age = 4000
'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'
'Hello, my name is Al. I am 4000 years old.'
'In ten years I will be ' + str(age + 10)
'In ten years I will be 4010'
# this is the old way


name = 'Al'
age = 4000
f'My name is {name}. I am {age} years old.'
'My name is Al. I am 4000 years old.'
f'In ten years I will be {age + 10}'
'In ten years I will be 4010'

''' Everything between the curly brackets ({}) is interpreted as if it were passed to str()
  and concatenated with the + operator in the middle of the string '''

'''If you need to use literal curly bracket characters in an f-string, use two curly brackets:'''

name = 'Zophie'
f'{name}'
'Zophie'
f'{{name}}'  # Double curly brackets are literal curly brackets.
'{name}'

spam = 'Hello, world!'
spam = spam.upper()
spam
'HELLO, WORLD!'
spam = spam.lower()
spam
'hello, world!'

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

spam = 'Hello, world!'
spam.islower()
False
spam.isupper()
False
'HELLO'.isupper()
True
'abc12345'.islower()
True
'12345'.islower()
False
'12345'.isupper()
False

'Hello'.upper()
'HELLO'
'Hello'.upper().lower()
'hello'
'Hello'.upper().lower().upper()
'HELLO'
'HELLO'.lower()
'hello'
'HELLO'.lower().islower()
True

'''
isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers (alphanumerics) and isn’t blank

isdecimal() Returns True if the string consists only of numeric characters and isn’t blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and isn’t blank

istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters'''

'hello'.isalpha()
True
'hello123'.isalpha()
False
'hello123'.isalnum()
True
'hello'.isalnum()
True
'123'.isdecimal()
True
'-5'.isdecimal()
False             # the '-' is an invalid character
'4.2'.isdecimal()
False             # the '.' is an invalid character
'    '.isspace()
True
'This Is Title Case'.istitle()
True



while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
# when this program ^ is run
# the output looks like that v

'''
Enter your age:
forty two
Please enter a number for your age.
Enter your age:
42
Select a new password (letters and numbers only):
secr3t!
Passwords can only have letters and numbers.
Select a new password (letters and numbers only):
secr3t'''


'Hello, world!'.startswith('Hello')
True
'Hello, world!'.endswith('world!')
True
'abc123'.startswith('abcdef')
False
'abc123'.endswith('12')
False
'Hello, world!'.startswith('Hello, world!')
True
'Hello, world!'.endswith('Hello, world!')
True

'report_final.pdf'.endswith('.pdf')
True
'Hello, world!'.startswith('hello')
False


', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'

' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'

'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

'My name is Simon'.split()
['My', 'name', 'is', 'Simon']

'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']

'My name is Simon'.split('m')
['My na', 'e is Si', 'on']

spam = '''Dear Alice,
... There is a milk bottle in the fridge
... that is labeled "Milk Experiment."
...
... Please do not drink it.
... Sincerely,
... Bob'''
...
spam.split('\n')
['Dear Alice,', 'There is a milk bottle in the fridge',
'that is labeled "Milk Experiment."', '', 'Please do not drink it.',
'Sincerely,', 'Bob']

'Hello'.rjust(10)
'     Hello'

'Hello'.rjust(20)
'              Hello'

'Hello, World'.rjust(20)
'         Hello, World'

'Hello'.ljust(10)
'Hello     '

'Hello'.rjust(20, '*')
'***************Hello'

'Hello'.ljust(20, '-')
'Hello---------------'

'Hello'.center(20)
'       Hello        '

'Hello'.center(20, '=')
'=======Hello========'

spam = '    Hello, World    '
spam.strip()
'Hello, World'

spam.lstrip()
'Hello, World    '

spam.rstrip()
'    Hello, World'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
'BaconSpamEggs'


'Unicode code point'
ord('A')
65
ord('4')
52
ord('!')
33
chr(65)
'A'
'These functions are useful when you need to order or perform a mathematical operation on characters:'

ord('B')
66
ord('A') < ord('B')
True
chr(ord('A'))
'A'
chr(ord('A') + 1)
'B'

'''Ned Batchelder’s 2012 PyCon talk, “Pragmatic Unicode, or
How Do I Stop the Pain?”'''




