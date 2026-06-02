'''
Section 4: Regex (Ch 9)
Test: Build this in 25 minutes:
Build a simple validator:
- Validate email format (has @, has ., no spaces)
- Validate phone (10 digits, any format)
- Return True/False with error message
Pass: Wrote patterns from memory or near-memory
Fail: No idea where to start without looking it up
'''

import re

def validate_email(user_email):
    pattern = re.compile(r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$')
    match = pattern.search(user_email)
    if match:
        print('valid email')
        return True
    else:
        print('invalid')
        return False

def validate_phone(user_phone):
    pattern = re.compile(r'\d')
    match = pattern.findall(user_phone)
    if len(match) == 10:
        print('valid Phone Number')
        return True
    else:
        print('invalid phone number')
        return False

user_email = input('enter a valid email ex. JohnSmith@email.com:\n')
email_test = validate_email(user_email)
user_phone = input('\nenter: your 10 digit Phone number: \n')
phone_test = validate_phone(user_phone)

if email_test and phone_test:
    print('Pass')
else:
    print('Fail')















