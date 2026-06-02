'''
Write a program that uses regex to validate a password. A valid password must:

Be at least 8 characters long
Contain at least one uppercase letter
Contain at least one lowercase letter
Contain at least one digit
Contain at least one special character from !@#$%^&*

Test it with:
pythonpasswords = ['Hello1!', 'hello123!', 'HELLO123!', 'Hello123', 'Hello1!x']
Print "Valid" or "Invalid" for each.
Hint — use a separate re.search() check for each requirement rather than one complex pattern.'''


import re

passwords = ['Hello1!', 'hello123!', 'HELLO123!', 'Hello123', 'Hello1!x']

for password in passwords:
    if (len(password) >= 8
        and re.search(r'[A-Z]', password)
        and re.search(r'[a-z]', password)
        and re.search(r'\d', password)
        and re.search(r'[!@#$%^&*]', password)):
        print(password + ' valid')
    else:
        print(password + ' invalid')








