'''
Drill 2 — Assert with try/except
Write a function called validate_input that takes a username and password and runs four assertions:

Username is at least 3 characters
Password is at least 6 characters
Username and password are not the same
Password contains at least one number

Wrap each assert in its own try/except and print a specific message for each failure.
Return True if all pass, False if any fail.
'''

import re

def validate_input(username , password):
    pattern = re.compile(r'\d+') #?[A-Z]?[a-z]
    match = pattern.search(password)
    try:
        assert len(username) >= 3
    except AssertionError:
        print('user name must be longer than 3 characters')
        return False
    try:
        assert username != password
    except AssertionError:
        print('username and password cant be the same')
        return False
    try:
        assert len(password) >= 6
    except AssertionError:
        print('password must be longer then 6 characters')
        return False
    try:
        assert match is not None
    except AssertionError:
        print('password must have atleast 1 number')
        return False
    return True

username = False
password = False

while True:
    username = input('enter a username: ')
    password = input('enter a password: ')
    if validate_input(username, password):
        print(f'Welcome {username}')
        break
    else:
        continue

















