# CH5 - Debugging, Assertions, Logging
# Setup -> validate -> log -> handle errors -> disable

import logging
logging.basicConfig(level=logging.DEBUG)

def calculate_average(numbers):
    logging.debug(f"Calculating average of {numbers}")
    assert len(numbers) > 0, "List cannot be empty"
    total = 0
    for number in numbers:
        assert isinstance(number, (int, float)), f"{number} is not a number"
        total = total + number
    average = total / len(numbers)
    logging.debug(f"Average calculated: {average}")
    return average

def get_numbers():
    numbers = []
    while True:
        try:
            entry = input("Enter a number or 'done' to finish: ")
            if entry == "done":
                break
            numbers.append(float(entry))
            logging.debug(f"Added {entry} to list")
        except ValueError:
            logging.warning(f"Invalid entry: {entry}")
            print("Please enter a valid number.")
    return numbers

numbers = get_numbers()

if len(numbers) == 0:
    print("No numbers entered.")
else:
    average = calculate_average(numbers)
    print(f"Average: {average}")

logging.disable(logging.CRITICAL)
'''
Plain English logic walk through:

1 get_numbers() — loops until user types done, catches invalid input with ValueError, logs each addition
2 calculate_average() — asserts list is not empty and all items are numbers before processing
3 Logs inputs and results throughout
4 Main block checks if list is empty before calling calculate
5 Logging disabled at the end
'''

Examples

"1. Try / Except with Multiple Errors"
try:
    _______ = int(input(_______))
    _______
except _______:
    print(_______)
except _______:
    print(_______)


try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("That is not a valid number.")
'''
Plain English:
try runs the code. If a specific error occurs Python jumps to the matching except block.
You can stack multiple except blocks for different error types.
Put int(input()) inside try so ValueError gets caught when the user types letters.

Use cases:
Any user input that gets converted to a number
File operations that could fail
Any operation with predictable failure points
'''


"2. Assertions"
assert _______, "_______"


age = 25
assert age >= 0, "Age cannot be negative"

stock = 10
assert stock > 0, "Stock cannot be empty"

assert False  # always triggers
'''
Plain English:
Assert checks if a condition is True.
If it's False the program immediately crashes with an AssertionError and prints your message.
Used as a sanity check — "this should always be true, stop everything if it isn't."

Use cases:
Checking that data is valid before processing it
Catching bugs during development
Making sure function inputs make sense
'''


"3. Basic Logging Setup"
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug(_______)
logging.info(_______)
logging.warning(_______)
logging.error(_______)
logging.critical(_______)


import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("Starting program")
logging.info("User logged in")
logging.warning("Low memory warning")
logging.error("File not found")
logging.critical("System failure")
'''
Plain English:
Logging records what your program is doing as it runs.
Five levels from least to most severe — DEBUG, INFO, WARNING, ERROR, CRITICAL.
Setting the level filters out everything below it.

Use cases:
Tracking program flow during development
Recording errors in production
Replacing print statements during debugging
'''


"4. Logging to a File"
import logging
logging.basicConfig(
    filename=_______,
    level=logging.DEBUG
)


import logging
logging.basicConfig(
    filename='programLog.txt',
    level=logging.DEBUG
)

logging.debug("Program started")
logging.warning("Something looks wrong")
'''
Plain English:
Instead of printing to the console, logs get written to a text file.
Useful for longer programs where you need a record of what happened.

Use cases:
Saving a record of errors for review later
Tracking user activity in a program
'''


"5. Disabling Logging"
logging.disable(logging.CRITICAL)


import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("This shows during development")

logging.disable(logging.CRITICAL)

logging.debug("This never shows")
logging.critical("This never shows either")
'''
Plain English:
One line silences all logging at and below the specified level.
logging.CRITICAL is the highest level so it silences everything.
Place it at the top when you're done debugging to turn off all logs without deleting them.

Use cases:
Switching from development to production
Temporarily silencing debug noise
'''


"6. Logging Inside Functions"
import logging
logging.basicConfig(level=logging.DEBUG)

def _______(_______):
    logging.debug(_______)
    try:
        _______
        logging.debug(_______)
        return _______
    except _______:
        logging.error(_______)

logging.disable(logging.CRITICAL)


import logging
logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted")

result = divide(10, 2)
print(result)

logging.disable(logging.CRITICAL)
'''
Plain English:
Log at the start of the function to record inputs,
log after key operations to record results,
log in except blocks to record errors. Always disable logging at the end of the program.

Use cases:
Tracing exactly what a function received and returned
Recording which errors occurred and when
'''


Extra

isinstance() is how you ask Python:

“Is this value a certain type?”

Basic shape:
isinstance(value, type)

It gives back either:

True if the value matches the type
False if it does not

One example
spam = 5

if isinstance(spam, int):
    print("spam is an integer")
else:
    print("spam is not an integer")

Output:

spam is an integer





