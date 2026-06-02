'''
Write a program that uses regex to check if a string is a valid US phone number
in the format ###-###-####.
Test it with:

"415-555-1234" → valid
"415-5555-1234" → invalid
"hello" → invalid

Print "Valid" or "Invalid" for each.'''

import re
phone_number = re.compile(r'^\d{3}-\d{3}-\d{4}$')
maybe_numbers = ('415-555-1234', '415-5555-1234', 'hello')


for number in maybe_numbers:
    if phone_number.search(number) is not None:
            print (number + ' valid')
    else:
            print (number + ' invalid')





