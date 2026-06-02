# Write a program that: Asks the user for two numbers
# Has a function called safe_divide that takes two numbers, logs both inputs, divides them, logs the result and returns it
# Uses try/except to handle both ZeroDivisionError and ValueError
# Uses an assert to make sure neither number is negative before dividing
# Disables logging at the end



import logging
logging.basicConfig(level=logging.DEBUG)

def safe_divide():
    num1 = int(input('type first number '))
    logging.debug(num1)
    num2 = int(input('type second number '))
    logging.debug(num2)
    assert num1 >= 0
    assert num2 >= 0
    try:
        result = num1 / num2
        logging.debug(result)
        return result
    except ZeroDivisionError:
        logging.debug("Cannot divide by zero")
    except ValueError:
        logging.debug("Please enter a valid number")
result = safe_divide()
print(result)
logging.disable(logging.CRITICAL)
