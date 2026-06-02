'''
Write a program that asks the user to enter a binary number,
validates it contains only 0s and 1s,
converts it to decimal and hex, and prints all three.
'''

import re
def get_numbies(choice):
    decimal = choice
    hex_str = hex(choice)[2:].upper()
    binary = bin(choice)[2:]
    october = oct(choice)[2:]
    return decimal, hex_str, binary, october
pattern = re.compile(r'^[01]+$')
while True:
    choice = input('enter a binary num: ')
    if not pattern.search(choice):
            print ("only '1' or '0'")
            continue
    choice = int(choice, 2)
    gort = get_numbies(choice)
    print(gort)


























