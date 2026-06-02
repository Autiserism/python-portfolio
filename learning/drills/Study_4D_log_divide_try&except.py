# Write a program that:
# Has a function called divide that takes two numbers and returns the result
# Uses logging.debug() to log both numbers before dividing and log the result after
# Uses try/except to handle division by zero
# Disables all logging at the end

import logging
logging.basicConfig(level=logging.DEBUG)

num1 = 10
num2 = 0

def divide(num1, num2):
    try:
        logging.debug(num1)
        logging.debug(num2)
        result = num1 / num2
        logging.debug(result)
        return result

    except ZeroDivisionError:
        logging.debug("Cannot divide by zero")
result = divide(num1, num2)
print(result)
logging.disable(logging.CRITICAL)
