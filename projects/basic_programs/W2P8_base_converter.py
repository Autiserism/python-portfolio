'''
W2P8 — Number Base Converter
Ask for a number and convert it
between decimal, binary and hexadecimal.
Menu driven. Use try/except for invalid input. Display all three formats.
'''

def get_all_formats(decimal_num):
    decimal = decimal_num
    binary = bin(decimal_num)[2:] # wouldent have gotten
    hexadec = hex(decimal_num)[2:].upper() # wouldent have gotten
    return decimal, binary, hexadec

def print_formats(decimal, binary, hexadec):
    print(f'Decimal:     {decimal}')
    print(f'Binary:      {binary}')
    print(f'Hexadecimal: {hexadec}')

while True:
    print(''' menu
    1 enter decimal, 2 enter binary, 3 enter hexadecimal, 9 quit''')
    try:
        choice = int(input('enter a number: '))
    except ValueError:
        continue
    if choice == 1:
        try:
            num = int(input('enter decimal number: '))
        except ValueError:
            print('invalid')
            continue
        decimal, binary, hexadec = get_all_formats(num)
        print_formats(decimal, binary, hexadec)
    elif choice == 2:
        try:
            num = int(input('enter binary number: '), 2) # wouldent have gotten
        except ValueError:
            print('invalid binary')
            continue
        decimal, binary, hexadec = get_all_formats(num)
        print_formats(decimal, binary, hexadec)
    elif choice == 3:
        try:
            num = int(input('enter hex number: '), 16) # wouldent have gotten
        except ValueError:
            print('invalid hex')
            continue
        decimal, binary, hexadec = get_all_formats(num)
        print_formats(decimal, binary, hexadec)
    elif choice == 9:
        break




















