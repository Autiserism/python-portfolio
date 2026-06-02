# CH8 - Strings
# Input -> clean -> validate -> format -> output

def clean_input(text):
    text = text.strip()
    text = ' '.join(text.split())
    return text.title()

def is_valid_name(name):
    for char in name:
        if not char.isalpha() and char != ' ':
            return False
    return True

def is_palindrome(text):
    text = ''.join(text.split()).lower()
    return text == text[::-1]

def censor(text, banned):
    words = text.split()
    result = []
    for word in words:
        if word.lower() in banned:
            result.append('*' * len(word))
        else:
            result.append(word)
    return ' '.join(result)

# Main program
name = input("Enter your full name: ")
name = clean_input(name)

if is_valid_name(name):
    parts = name.split()
    first = parts[0]
    last = parts[-1]
    print(f"\nFirst name: {first}")
    print(f"Last name: {last}")
    print(f"Initials: {first[0]}.{last[0]}.")
    print(f"Name reversed: {name[::-1]}")
    print(f"Is palindrome: {is_palindrome(name)}")
else:
    print("Invalid name - letters only please.")

sentence = input("\nEnter a sentence: ")
banned = ["bad", "wrong", "terrible"]
print(censor(sentence, banned))
'''
Plain English logic walk through:

1 clean_input() — strips edges, removes extra spaces, applies title case
2 is_valid_name() — loops through each character checking it's a letter or space
3 is_palindrome() — removes spaces, lowercases, compares to its reverse
4 censor() — splits into words, replaces banned words with asterisks, rejoins
5 Main block — cleans input first, validates it, then runs multiple string operations and formats output with f-strings
'''

Examples


"1. String Basics and Escape Sequences"
_______ = "_______"
_______ = '_______'
_______ = """_______
_______"""
_______ = r"_______"  # raw string


name = "Gman"
quote = 'He said "hello"'
multiline = """This is
a multiline
string"""
path = r"C:\Users\Gman\Documents"  # raw string ignores \

# Escape sequences
newline = "Hello\nWorld"    # new line
tab = "Hello\tWorld"        # tab
backslash = "C:\\Users"     # literal backslash
apostrophe = 'It\'s fine'   # apostrophe in single quotes
'''
Plain English:
Strings can use single or double quotes.
Triple quotes allow multi-line strings.
Raw strings treat backslashes as literal characters — useful for file paths and regex.
Escape sequences let you put special characters inside strings.

Use cases:
Raw strings for file paths and regex patterns
Multi-line strings for long messages or docstrings
Escape sequences for formatting output
'''


"2. String Indexing and Slicing"
_______[_______]          # single character
_______[_______:_______]  # slice
_______[:_______]         # from start
_______[_______:]         # to end
_______[::-1]             # reverse
_______[i:i+n]            # sliding window - n chars from position i


text = "Hello, world!"
text[0]       # 'H'
text[-1]      # '!'
text[0:5]     # 'Hello'
text[:5]      # 'Hello'
text[7:]      # 'world!'
text[::-1]    # '!dlrow ,olleH'
text[0:3]     # 'Hel'
text[1:4]     # 'ell'
text[2:5]     # 'llo'
'''
Plain English:
Strings work like lists for indexing and slicing.
Index starts at 0. Negative indexes count from the end.
Slicing grabs from start up to but not including the end index.
[::-1] reverses the string.
[i:i+n] grabs n characters starting at position i — useful for sliding through a string.

Use cases:
Extracting parts of a string
Reversing a string for palindrome checks
Sliding window for pattern searching
'''


"3. Case and Checking Methods"
_______.upper()             # ALL CAPS
_______.lower()             # all lowercase
_______.title()             # Title Case
_______.capitalize()        # First letter only
_______.isupper()           # True if all uppercase
_______.islower()           # True if all lowercase
_______.isalpha()           # True if only letters
_______.isdecimal()         # True if only numbers
_______.isalnum()           # True if letters and numbers
_______.isspace()           # True if only whitespace
_______.startswith(_______) # True if starts with
_______.endswith(_______)   # True if ends with



text = "Hello World"
text.upper()           # "HELLO WORLD"
text.lower()           # "hello world"
text.title()           # "Hello World"
text.isupper()         # False
"abc123".isalnum()     # True
"12345".isdecimal()    # True
text.startswith("He")  # True
text.endswith("ld")    # True
'''
Plain English:
String methods never modify the original — always reassign.
text.upper() does nothing on its own. text = text.upper() updates it.
Methods can be chained — text.strip().lower().title() runs left to right.

Use cases:
Normalizing user input before comparing
Validating that input contains only certain character types
Formatting names and titles
'''


"4. Searching and Replacing"
_______.find(_______)           # index of first match or -1
_______.replace(_______, _______) # replace all occurrences
_______ in _______              # True if substring exists
_______ not in _______          # True if substring missing


text = "Hello, world!"
text.find("world")        # 7
text.find("xyz")          # -1
text.replace("world", "Python")  # "Hello, Python!"
"world" in text           # True
"xyz" not in text         # True
'''
Plain English:
.find() returns the index of the first match or -1 if not found.
.replace() returns a new string with all matches replaced — it doesn't modify the original.
in and not in are simpler when you just need True or False.

Use cases:
Finding where a substring appears
Censoring or replacing words
Checking if a string contains a keyword
'''


"5. Splitting and Joining"
_______.split()           # split on whitespace
_______.split(_______)    # split on delimiter
_______.join(_______)     # join list into string
_______.strip()           # remove whitespace both ends
_______.lstrip()          # remove whitespace left
_______.rstrip()          # remove whitespace right


# Split
"hello world".split()          # ['hello', 'world']
"a,b,c".split(',')             # ['a', 'b', 'c']
"  hello  world  ".split()     # ['hello', 'world'] - removes extra spaces

# Join
' '.join(['hello', 'world'])   # 'hello world'
'-'.join(['a', 'b', 'c'])      # 'a-b-c'
''.join(['a', 'b', 'c'])       # 'abc'

# Strip
"  hello  ".strip()            # 'hello'
"  hello  ".lstrip()           # 'hello  '
"  hello  ".rstrip()           # '  hello'
'''
Plain English:
split() breaks a string into a list. join() puts a list back into a string.
They are opposites and work together constantly.
split() without arguments removes all extra whitespace automatically.
strip() cleans up the edges of a string.

Use cases:
Breaking a sentence into individual words
Cleaning user input
Building formatted strings from lists
'''


"6. Padding and Alignment"
_______.rjust(_______, _______)  # right align with padding
_______.ljust(_______, _______)  # left align with padding
_______.center(_______, _______) # center with padding


'hello'.rjust(10)         # '     hello'
'hello'.ljust(10)         # 'hello     '
'hello'.center(10)        # '  hello   '
'hello'.rjust(10, '*')    # '*****hello'
'hello'.center(10, '-')   # '--hello---'
'''
Plain English:
Pads a string to a set width with spaces or a chosen character.
Useful for creating neat columns of text.
The number sets the total width including the string itself.

Use cases:
Formatting tables and reports
Creating neat menu displays
'''


"7. F-Strings"
f"_______ {_______} _______"
f"_______ {_______.method()} _______"
f"_______ {_______:.2f} _______"


name = "Gman"
age = 25
price = 3.14159

f"Hello {name}"                  # 'Hello Gman'
f"Age: {age}"                    # 'Age: 25' - no str() needed
f"Price: {price:.2f}"            # 'Price: 3.14'
f"Name: {name.upper()}"          # 'Name: TYLER'
f"Result: {10 * 5}"              # 'Result: 50'
'''
Plain English:
Put f before the opening quote.
Anything inside {} gets evaluated and inserted into the string.
No need to convert numbers to strings.
Any valid Python expression works inside the braces including method calls and math.

Use cases:
Any time you combine variables with text
Formatting numbers to a specific number of decimal places
Replacing all string concatenation with +
'''


"8. Character Values"
ord(_______)   # character to number
chr(_______)   # number to character


ord('A')    # 65
ord('a')    # 97
ord('0')    # 48
chr(65)     # 'A'
chr(97)     # 'a'
'''
Plain English:
Every character has a numeric value.
ord() converts a character to its number.
chr() converts a number back to a character.
Uppercase letters are 65-90, lowercase are 97-122.

Use cases:
Encryption and cipher programs
Checking if characters are in a certain range
Converting between letters and numbers
'''





