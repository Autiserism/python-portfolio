# CH9 - Regular Expressions
# compile -> search/findall -> group -> sub

import re

# Patterns
phone_pattern = re.compile(
    r'(?:\d{3})-(?:\d{3})-(?:\d{4})', re.VERBOSE)

email_pattern = re.compile(
    r'[a-zA-Z0-9%+\-_.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

password_pattern_upper = re.compile(r'[A-Z]')
password_pattern_lower = re.compile(r'[a-z]')
password_pattern_digit = re.compile(r'\d')
password_pattern_special = re.compile(r'[!@#$%^&*]')

def validate_phone(text):
    if phone_pattern.search(text) is not None:
        return True
    return False

def find_emails(text):
    return email_pattern.findall(text)

def validate_password(password):
    if (len(password) < 8):
        return "Too short"
    if not password_pattern_upper.search(password):
        return "Needs uppercase letter"
    if not password_pattern_lower.search(password):
        return "Needs lowercase letter"
    if not password_pattern_digit.search(password):
        return "Needs a number"
    if not password_pattern_special.search(password):
        return "Needs a special character"
    return "Valid"

def censor_numbers(text):
    def replace(match):
        return '#' * len(match.group())
    return re.sub(r'\d', replace, text)

# Main
print("=== Phone Validator ===")
phones = ["415-555-1234", "123-45-6789", "hello"]
for phone in phones:
    result = "Valid" if validate_phone(phone) else "Invalid"
    print(f"{phone}: {result}")

print("\n=== Email Finder ===")
text = "Contact support@example.com or sales@company.org for help."
emails = find_emails(text)
print(f"Found: {emails}")

print("\n=== Password Validator ===")
passwords = ["Hello1!x", "hello123!", "HELLO123!", "Hi1!"]
for password in passwords:
    print(f"{password}: {validate_password(password)}")

print("\n=== Number Censor ===")
text = "Call 555-1234 or 800-555-9876 for info."
print(censor_numbers(text))
'''
Plain English logic walk through:

1 All patterns compiled once at the top — not inside functions
2 validate_phone() — returns True or False using .search() is not None
3 find_emails() — returns a list using .findall()
4 validate_password() — checks each requirement separately, returns specific failure message
5 censor_numbers() — uses .sub() with a function for dynamic replacement
6 Main block — tests each function with sample data
'''

Method                      Returns                             Use when

.search()                   Match object or None                Finding first match
.findall()                  List of strings                     Finding all matches
.findall() with groups      List of tuples                      Extracting grouped data
.sub()                      Modified string                     Replacing matches
.group(0)                   Full match string                   Getting the full match
.group(n)                   Captured group string               Getting a specific part
.groups()                   Tuple of all groups                 Getting all parts at once


Examples


"1. Basic Setup"
import re
_______ = re.compile(r'_______')
_______ = _______.search(_______)
_______ = _______.findall(_______)


import re
pattern = re.compile(r'\d+')
match = pattern.search("My number is 42")
results = pattern.findall("1 cat, 2 dogs, 3 birds")

if match is not None:
    print(match.group())   # '42'

print(results)             # ['1', '2', '3']
'''
Plain English:
re.compile() builds a pattern object from a raw string.
.search() finds the first match and returns a match object or None.
.findall() finds all matches and returns a list.
Always check if .search() returned None before calling .group().

Use cases:
Validating input formats like phone numbers and emails
Extracting specific data from text
Finding patterns inside large strings
'''


        . Core Syntax
r'\d'    # any digit 0-9
r'\w'    # any letter, digit or underscore
r'\s'    # any whitespace
r'\D'    # anything NOT a digit
r'\W'    # anything NOT a word character
r'\S'    # anything NOT whitespace
r'.'     # any character except newline
r'^'     # start of string
r'$'     # end of string
r'\b'    # word boundary


re.compile(r'\d\d\d')      # three digits
re.compile(r'\w+')         # one or more word characters
re.compile(r'^\d+$')       # entire string is digits only
re.compile(r'\bcat\b')     # word 'cat' not inside another word
'''
Plain English:
Special sequences match categories of characters.
Uppercase versions match the opposite.
^ and $ anchor the pattern to the start and end of the string —
without them the pattern can match anywhere inside the string.
Use cases:

\d for numbers, \w for words, \s for whitespace
^ and $ for validating entire strings like passwords and phone numbers
\b for finding whole words only
'''


"3. Quantifiers"
r'_______*'      # 0 or more
r'_______+'      # 1 or more
r'_______?'      # 0 or 1 - optional
r'_______{n}'    # exactly n times
r'_______{n,m}'  # between n and m times
r'_______+?'     # lazy - as few as possible
r'_______*?'     # lazy - as few as possible



re.compile(r'\d+')        # one or more digits
re.compile(r'\d{3}')      # exactly 3 digits
re.compile(r'\d{3,5}')    # 3 to 5 digits
re.compile(r'colou?r')    # color or colour - u is optional
re.compile(r'\d+?')       # lazy - matches as few digits as possible
'''
Plain English:
Quantifiers control how many times a pattern repeats.
Greedy by default — matches as much as possible.
Add ? after a quantifier to make it lazy — matches as little as possible.

Use cases:
+ for one or more digits in a phone number
{n} for exact length like a 4 digit PIN
? for optional characters like country codes
Lazy matching when greedy takes too much
'''


"4. Groups and the Pipe"
r'(_______ | _______)'     # match either
r'(_______ ) (_______ )'   # capture groups
_______.group(0)            # full match
_______.group(1)            # first group
_______.group(2)            # second group
_______.groups()            # all groups as tuple


# Pipe - match either
pattern = re.compile(r'cat|dog')
pattern.search("I have a cat")   # matches 'cat'

# Groups
pattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
match = pattern.search("Call 415-555-1234")
match.group(0)    # '415-555-1234' - full match
match.group(1)    # '415' - area code
match.group(2)    # '555-1234' - number
match.groups()    # ('415', '555-1234')
'''
Plain English:
Parentheses create capture groups — they extract specific parts of a match.
| means OR — match the left pattern or the right.
group(0) always returns the full match. group(1) onwards returns individual captured groups.

Use cases:
Extracting area codes from phone numbers
Capturing first and last name separately
Matching multiple valid formats with |
'''


"5. Character Classes"
r'[_______]'          # match any character in set
r'[^_______]'         # match any character NOT in set
r'[a-z]'              # lowercase letters
r'[A-Z]'              # uppercase letters
r'[0-9]'              # digits
r'[a-zA-Z0-9]'        # letters and digits
r'[aeiou]'            # vowels only


re.compile(r'[aeiou]')        # any vowel
re.compile(r'[^aeiou]')       # anything that is not a vowel
re.compile(r'[A-Z][a-z]+')    # capital letter followed by lowercase
re.compile(r'[0-9a-f]')       # hex characters
re.compile(r'[!@#$%^&*]')     # special characters
'''
Plain English:
Square brackets define a set of characters to match.
A dash creates a range.
^ at the start of a character class means NOT — match anything except these characters.

Use cases:
Matching vowels or consonants
Validating passwords contain special characters
Matching hex values or specific character sets
'''


"6. Non-Capturing Groups"
r'(?:_______)'        # group without capturing


# Without non-capturing group - findall returns only the group
pattern = re.compile(r'(0[1-9]|1[0-2])/\d{2}/\d{4}')
pattern.findall("Date: 01/15/2023")   # ['01'] - only captures group

# With non-capturing group - findall returns full match
pattern = re.compile(r'(?:0[1-9]|1[0-2])/\d{2}/\d{4}')
pattern.findall("Date: 01/15/2023")   # ['01/15/2023'] - full match
'''
Plain English:
(?:...) groups without capturing.
Use it when you need to group part of a pattern for | or quantifiers
but don't want findall() to return just that part.
Regular () captures — (?:) groups without capturing.

Use cases:
Using | inside a larger pattern without affecting findall() output
Grouping for quantifiers without capturing
'''


"7. Substitution"
_______ = _______.sub('_______', _______)

# With function
def _______(match):
    return _______

_______ = _______.sub(_______, _______)


pattern = re.compile(r'\d+')

# Simple replacement
result = pattern.sub('X', "Call 555-1234")   # 'Call X-X'

# Function replacement
def censor(match):
    return '#' * len(match.group())

result = pattern.sub(censor, "Call 555-1234")  # 'Call ###-####'
'''
Plain English:
.sub() finds all matches and replaces them.
Pass a string for a fixed replacement.
Pass a function for dynamic replacement —
the function receives the match object and returns what to replace it with.

Use cases:
Censoring sensitive information
Replacing all numbers or names in a string
Formatting matched text dynamically
'''


"8. Flags"
re.compile(r'_______', re.IGNORECASE)  # case insensitive
re.compile(r'_______', re.DOTALL)      # dot matches newline
re.compile(r'''
    _______  # comment
    _______  # comment
''', re.VERBOSE)                        # readable multiline pattern


# Case insensitive
pattern = re.compile(r'hello', re.IGNORECASE)
pattern.search("HELLO world")   # matches

# Dotall - dot matches newlines
pattern = re.compile(r'.*', re.DOTALL)

# Verbose - add comments and whitespace
pattern = re.compile(r'''
    \d{3}    # area code
    -        # separator
    \d{3}    # prefix
    -        # separator
    \d{4}    # line number
''', re.VERBOSE)

# Multiple flags
pattern = re.compile(r'hello', re.IGNORECASE | re.DOTALL)
'''
Plain English:
Flags modify how the pattern works.
re.IGNORECASE matches regardless of case.
re.DOTALL makes . match newlines too.
re.VERBOSE lets you spread a pattern across multiple lines with comments.
Combine flags with |.

Use cases:
re.IGNORECASE for case insensitive searches
re.VERBOSE for complex patterns that need explanation
re.DOTALL when matching across multiple lines
'''




