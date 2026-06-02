#W3P1 — Input Validator W3P1_input_validator.py
#Build a xform validator using regex.
#Validate: full name, phone number, email address, date of birth, postal code.
#Print valid or invalid with specific error messages for each field.

import re

# Patterns with anchors
patternFN = re.compile(r'^[A-Za-z-]+(?:\s[A-Z]\.?)?\s[A-Za-z-]+$')
patternPN = re.compile(r'^(?:\+?1[\s\-\.]?)?(\(?\d{3}\)?)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})$')
patternEA = re.compile(r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$')
patternDB = re.compile(r'^(0[1-9]|1[0-2])[\s/.-]?(0[1-9]|[1-2][0-9]|3[0-1])[\s/.-]?(\d{4})$')
patternPC = re.compile(r'^[A-Za-z]\d[A-Za-z][\s.-]?\d[A-Za-z]\d$', re.IGNORECASE)

# Prompts and errors
name_prompt = 'Enter your first and last name: '
phone_prompt = 'Enter your phone number: '
email_prompt = 'Enter your email address: '
dob_prompt = 'Enter your date of birth (MM/DD/YYYY): '
postal_prompt = 'Enter your postal code (A1A 1A1): '

name_error = 'Must include first and last name, letters only'
phone_error = 'Must be format 555-555-5555'
email_error = 'Must include @ and domain like .com'
dob_error = 'Must be format MM/DD/YYYY'
postal_error = 'Must be format A1A 1A1'

def get_valid_input(prompt, pattern, error_message):
    while True:
        value = input(prompt).strip()  # Added .strip() to remove leading/trailing spaces
        if re.fullmatch(pattern, value):  # Changed to fullmatch
            return value
        print(f'Invalid: {error_message}')

def form_fill():
    full_name = get_valid_input(name_prompt, patternFN, name_error)
    phone_num = get_valid_input(phone_prompt, patternPN, phone_error)
    email = get_valid_input(email_prompt, patternEA, email_error)
    birthday = get_valid_input(dob_prompt, patternDB, dob_error)
    postal = get_valid_input(postal_prompt, patternPC, postal_error)

    form_info = {
        'name': full_name,
        'phone': phone_num,
        'email': email,
        'dob': birthday,
        'postal': postal
    }

    print('\n✓ Form completed successfully!')
    return form_info

form_data = form_fill()
print('\nForm Data:')
for field, value in form_data.items():
    print(f'  {field.title()}: {value}')

'''
import re

form_info = {}
#regex took lots of trial and error
patternFN = re.compile(r'^[A-Za-z]+(?:\s[A-Z]\.?)?\s[A-Za-z]+$')
patternPN = re.compile(r'^(?:\+?1[\s\-\.]?)?(\(?\d{3}\)?)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})$')
patternEA = re.compile (r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$') #(r'[\w._-]+@[\w._-]+\.[a-zA-Z]{2,4}')   #(r'([\w.-_]+)@([\w.-_]+)')
patternDB = re.compile(r'^(0[1-9]|1[0-2])[\s/.-]?(0[1-9]|[1-2][0-9]|3[0-1])[\s/.-]?(\d{4})$') #MM/DD/YYYY
patternPC = re.compile(r'^[A-Z]\d[A-Z][\s.-]?\d[A-Z]\d$', re.IGNORECASE)

name_prompt = 'Enter Your First and Last name\n'
phone_prompt = 'Enter your Phone number\n'
email_prompt = 'Enter your email adress\n'
dob_prompt = 'Enter your Date of Birth\n'
postal_prompt = 'Enter your postal code\n'
name_error = 'Must include first and last name, letters only'
phone_error = 'Must be format 555-555-5555'
email_error = 'Must include @ and domain like .com'
dob_error = 'Must be format MM/DD/YYYY'
postal_error = 'Must be format A1A 1A1'

def get_valid_input(prompt, pattern, error_message): #didnt think to use
    while True:
        value = input(prompt)
        if re.search(pattern, value):
            return value
        print(f'Invalid: {error_message}')

def form_fill():
    global form_info
    full_name = get_valid_input(name_prompt,patternFN, name_error)
    phone_num = get_valid_input(phone_prompt,patternPN, phone_error)
    email = get_valid_input(email_prompt,patternEA, email_error)
    birthday = get_valid_input(dob_prompt,patternDB, dob_error)
    postal = get_valid_input(postal_prompt,patternPC, postal_error)
    form_info = {full_name : {'Phone': phone_num, 'Email': email, 'DOB': birthday, 'Mail': postal}}
    print('done')

form_fill()
print(form_info)

#'HIGHLAND B. COW'
#'555-944-4235'
#'sir-beef@Moo.feed'
#'06/10/2025'
#'G0D 1S1'
'''

















