'''
Write a function that takes a decimal number
and prints a full conversion table showing binary,
octal oct() and hexadecimal. Test with 5 numbers.
'''

def get_numbies(number):
    decimal = number
    bin_str = bin(number)[2:]
    hex_str = hex(number)[2:].upper()
    octal = oct(number)[2:]
    return decimal, bin_str, hex_str, octal



gort = get_numbies(4000)
print (gort)

























