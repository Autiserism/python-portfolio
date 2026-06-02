# CH1 - Basics
# Input -> convert -> math -> output

name = input("What is your name? ")
age = int(input("What is your age? "))
birth_year = 2026 - age

print(f"Hello {name}.")
print(f"You were born in {birth_year}.")
print(f"In 10 years you will be {age + 10}.")

'''
Plain English logic walk through:

1 Ask for name, store as string
2 Ask for age, convert to integer immediately
3 Calculate birth year using math
4 Print three lines using f-strings to combine variables and text
'''
Examples


"1. Printing Output"
print(_________)


print("Hello, world!")
print("My name is " + name)
print(f"My name is {name}")
'''
Plain English:
Display something on the screen. Can be a string, a variable, or a combination of both.

Use cases:
Showing results to the user
Checking what a variable contains while debugging
'''


"2. Getting Input"
_______ = input(_________)


name = input("What is your name? ")
'''
Plain English:
Ask the user to type something. Whatever they type gets stored in the variable. Always returns a string.

Use cases:
Asking a user for their name, age, password, or any information
'''


"3. Converting Types"
_______ = int(_________)
_______ = str(_________)
_______ = float(_________)


age = int(input("How old are you? "))
price = float(input("Enter price: "))
label = str(42)
'''
Plain English:
input() always returns a string. If you need a number to do math with, convert it first.
If you need to combine a number with a string, convert it to a string first.

Use cases:
Any time you do math with user input
Any time you print a number inside a sentence
'''


"4. Variables"
_______ = _______


name = "Gman"
age = 25
score = 0
is_valid = True
'''
Plain English:
A container that holds a value. You give it a name and assign it a value with =.
You can change it later by assigning it again.

Use cases:
Storing anything you need to use or change later in the program
'''


"5. Basic Math"
_______ = _______ + _______
_______ = _______ - _______
_______ = _______ * _______
_______ = _______ / _______
_______ = _______ % _______


total = price + tax
difference = high - low
area = width * height
average = total / count
remainder = 10 % 3   # returns 1
'''
Plain English:
Standard math operators. % is the modulo operator —
it returns the remainder after division. Useful for checking if a number is even or odd.

Use cases:
Calculating totals, averages, remainders
Checking divisibility with %
'''
