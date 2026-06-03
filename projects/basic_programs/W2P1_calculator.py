'''
Full calculator with add,
subtract, multiply, divide.
Menu driven.
Use try/except for division by zero and invalid input.
Log all calculations to a file using logging.
'''
# import logging
# import re
# logging.basicConfig(filename='calculatorlog.txt', level=logging.DEBUG)

# define add(a, b)
#     logging.debug(f'adding {a} + {b}')
#     result = a + b
#     logging.debug(f'result: {result}')
#     return result

# define subtract(a, b) same structure
# define multiply(a, b) same structure

# define divide(a, b)
#     logging.debug(f'dividing {a} / {b}')
#     try
#         result = a / b
#         logging.debug(f'result: {result}')
#         return result
#     except ZeroDivisionError
#         logging.error('division by zero attempted')
#         print cannot divide by zero
#         return None

# operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

# define get_numbers()
#     try
#         a = float(input('first number: '))
#         b = float(input('second number: '))
#         return a, b
#     except ValueError
#         logging.warning('invalid number input')
#         print invalid input
#         return None, None

# define regex_calculate(expression)
#     pattern = re.compile(r'(\d+\.?\d*)([+\-*/])(\d+\.?\d*)')
#     match = pattern.search(expression)
#     if match is None
#         print invalid expression
#         return
#     a = float(match.group(1))
#     operator = match.group(2)
#     b = float(match.group(3))
#     if operator in operations
#         result = operations[operator](a, b)
#         if result is not None
#             print result
#     else
#         print invalid operator

# while True
#     print menu options
#     1 add, 2 subtract, 3 multiply, 4 divide, 5 expression, 9 quit
#     try
#         choice = int(input)
#     except ValueError continue
#     logging.debug(f'choice: {choice}')
#     if choice in [1,2,3,4]
#         a, b = get_numbers()
#         if a is None continue
#         result = operations[{1:'+',2:'-',3:'*',4:'/'}[choice]](a, b)
#         if result is not None print result
#     elif choice == 5
#         expression = input('enter expression eg 5+3: ')
#         regex_calculate(expression)
#     elif choice == 9 break
#     else print invalid

# logging.disable(logging.CRITICAL)

import logging
import re

logging.basicConfig(filename='W2P1_calculatorProgramlog.txt',level=logging.DEBUG)

def add (a, b):
    logging.debug(f'adding: {a} + {b}')
    result = a + b
    logging.debug(f'result: {result}')
    return result

def subtract(a, b):
    logging.debug(f'subtracting: {a} - {b}')
    result = a - b
    logging.debug(f'result: {result}')
    return result


def multiply (a, b):
    logging.debug(f'multiplication: {a} * {b}')
    result = a * b
    logging.debug(f'result: {result}')
    return result


def divide(a, b):
    logging.debug(f'Division: {a} / {b}')
    try:
        result = a / b
        logging.debug(f'result: {result}')
        return result
    except ZeroDivisionError:
        logging.error('Divide by zero attempted')
        print('Cannot Divide by zero')
        return None

operations = {'+': add, '-' : subtract, '*' : multiply, '/' : divide}

def get_numbers ():
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        return a, b
    except ValueError:
        logging.error('invalid input')
        print ('invalid input')
        return None, None


def regex_calculate(expression):
    pattern = re.compile(r'(\d+\.?\d*)([+\-/*])(\d+\.?\d*)')
    match = pattern.search(expression)
    if match is None:
        print('invalid expression')
        return None
    a = float(match.group(1))
    operator = match.group(2)
    b = float(match.group(3))
    if operator in operations:
        result = operations[operator](a,b)
        if result is not None:
            print(result)
    else:
        print('invalid operator')


while True:
    print('''Calculator:
    1 add
    2 subtract
    3 multiply
    4 divide
    5 expression
    9 quit'''
    )
    try:
        choice = int(input('> '))
    except ValueError:
        continue
    logging.debug(f'choice: {choice}')
    if choice in [1,2,3,4]:
        a, b = get_numbers()
        if a is None:
            continue
        result = operations[{1:'+', 2:'-', 3:'*', 4:'/'}[choice]](a, b)
        if result is not None:
            print(result)
    elif choice == 5:
        expression= input('enter an expression eg 24+25: ')
        regex_calculate(expression)
    elif choice == 9:
        break
    else:
        print('invalid')

logging.disable(logging.CRITICAL)

