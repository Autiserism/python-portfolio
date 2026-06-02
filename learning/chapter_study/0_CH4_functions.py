# CH4 - Functions
# Define -> call -> return -> use result

lives = 3

def get_guess():
    try:
        guess = int(input("Guess a number 1-10: "))
        return guess
    except ValueError:
        print("Please enter a valid number.")
        return None

def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "too low"
    else:
        return "too high"

def lose_life():
    global lives
    lives = lives - 1
    print(f"Wrong! Lives remaining: {lives}")

secret = 7
print("Welcome to the guessing game.")

while lives > 0:
    guess = get_guess()
    if guess is None:
        continue
    result = check_guess(guess, secret)
    if result == "correct":
        print("You got it!")
        break
    else:
        print(f"Hint: {result}")
        lose_life()

if lives == 0:
    print(f"Game over. The number was {secret}.")
'''
Plain English logic walk through:

1 get_guess() — handles input and converts to integer safely, returns None if invalid
2 check_guess() — compares guess to secret, returns a result string
3 lose_life() — modifies the global lives variable, prints remaining lives
4 Main loop — calls each function in order, uses return values to decide what happens next
5 Each function does one job — input, checking, tracking lives
'''

Examples

"1. Defining and Calling a Function"
def _______():
    _______

_______()


def greet():
    print("Hello, world!")

greet()
'''
Plain English:
def creates a reusable block of code with a name.
Nothing inside it runs until you call it by name with (). Define first, call second.

Use cases:
Grouping code that does one specific job
Any code you need to run more than once
'''


"2. Functions with Arguments"
def _______(_______, _______):
    _______

_______(_______,  _______)


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Gman", 25)
'''
Plain English:
Arguments pass data into the function when you call it. Inside the function they act like variables.
The number of arguments in the call must match the number in the definition.

Use cases:
Any function that needs outside data to do its job
Making functions reusable with different inputs
'''


"3. Return Values"
def _______(_______):
    return _______

result = _______(_______)
print(result)


def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # 7
'''
Plain English:
return sends data back to whoever called the function.
The function exits immediately at return — nothing after it runs.
Always catch the return value in a variable or wrap the call in print() or the data disappears.

Use cases:
Any function that calculates or processes something and needs to send the result back
Building data to use elsewhere in the program
'''


"4. Local and Global Scope"
# Global variable
_______ = _______

def _______():
    # Local variable - only exists here
    _______ = _______

# Modifying global from inside function
def _______():
    global _______
    _______ = _______


score = 0  # global

def add_points():
    global score
    score = score + 10

def show_score():
    local_message = "Your score is"  # local only
    print(f"{local_message} {score}")

add_points()
show_score()
'''
Plain English:
Variables created inside a function only exist inside that function — local scope.
Variables created outside functions exist everywhere — global scope.
To modify a global variable from inside a function you must declare it with global first.

Use cases:
global — tracking a score, counter or state across multiple function calls
Local variables — keeping calculations contained inside a function
'''

"5. Try / Except"
def _______():
    try:
        _______
        return _______
    except _______:
        print(_______)


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input")

result = safe_divide(10, 2)
print(result)
'''
Plain English:
try runs the code. If an error occurs Python jumps to the matching except block instead of crashing.
Put int(input()) inside try to catch invalid user input with ValueError.

Use cases:
Any time user input is converted to a number
Division operations
Any operation that could fail with bad input
'''


"6. Multiple Return Values"
def _______(_______):
    return _______, _______

_______, _______ = _______(_______)


def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([3, 7, 2, 9, 4])
print(f"Low: {lowest}, High: {highest}")
'''
Plain English:
Functions can return more than one value separated by commas.
Catch them by unpacking into matching variables on the left side.

Use cases:
Returning both a result and a status
Returning multiple calculated values at once
'''




