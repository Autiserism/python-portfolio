# Write a program that uses logging to track a countdown from 10 to 0.
# Use logging.debug() to log each number as the loop counts down
# Set it up so logs display in the console.

import logging
logging.basicConfig(level=logging.DEBUG)
countdown = [10, 9, 8, 7,6 ,5 ,4 ,3 ,2 ,1]
def num_check(countdown):
    for ten in range(10, 0, -1):
        logging.debug(ten)
num_check(countdown)

