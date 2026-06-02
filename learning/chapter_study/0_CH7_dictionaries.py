# CH7 - Dictionaries
# Create -> access -> modify -> loop -> nested

import pprint

contacts = {
    'Gman': {'phone': '555-1234', 'email': 'Gman@email.com'},
    'Bob': {'phone': '555-5678', 'email': 'bob@email.com'},
    'Sarah': {'phone': '555-9012', 'email': 'sarah@email.com'}
}

def find_contact(contacts, name):
    return contacts.get(name, None)

def add_contact(contacts, name, phone, email):
    contacts.setdefault(name, {'phone': phone, 'email': email})
    return contacts

def display_contacts(contacts):
    for name, info in contacts.items():
        print(f"\n{name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")

while True:
    print("\n1. Find contact")
    print("2. Add contact")
    print("3. Display all")
    print("4. Quit")
    choice = input("Choose: ")

    if choice == '1':
        name = input("Enter name: ")
        result = find_contact(contacts, name)
        if result:
            print(f"Phone: {result['phone']}, Email: {result['email']}")
        else:
            print("Contact not found.")

    elif choice == '2':
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts = add_contact(contacts, name, phone, email)
        print(f"{name} added.")

    elif choice == '3':
        display_contacts(contacts)

    elif choice == '4':
        break
'''
Plain English logic walk through:

1 find_contact() — uses .get() to safely look up a contact, returns None if not found
2 add_contact() — uses .setdefault() to add only if name doesn't already exist
3 display_contacts() — loops through nested dictionaries displaying each contact's info
4 Main loop — menu driven program that keeps running until user quits
5 Each function does one job and returns data back to the main block
'''


Examples


"1. Creating and Accessing Dictionaries"
_______ = {_______: _______, _______: _______}
_______[_______]           # access by key
_______[_______] = _______  # add or update key
del _______[_______]        # delete key


person = {'name': 'Gman', 'age': 25, 'city': 'Windsor'}
person['name']          # 'Gman'
person['job'] = 'programmer'  # adds new key
person['age'] = 25      # updates existing key
del person['city']      # removes key
'''
Plain English:
A dictionary stores data as key-value pairs inside curly brackets.
Access values by their key name instead of an index position.
Add or update by assigning to a key. Delete with del.

Use cases:
Storing related data about one thing like a person or product
Any time data has a label and a value
Replacing multiple variables with one organized structure
'''


"2. Dictionary Methods"
_______.keys()     # all keys
_______.values()   # all values
_______.items()    # all key-value pairs

for _______ in _______.keys():
for _______ in _______.values():
for _______, _______ in _______.items():


person = {'name': 'Gman', 'age': 25}

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
'''
Plain English:
.keys() gives all the key names. .values() gives all the values.
.items() gives both together as pairs. Use these to loop through a dictionary cleanly.

Use cases:
Displaying all data in a dictionary
Searching through values
Building new structures from dictionary data
'''


"3. Safe Access with .get()"
_______.get(_______, _______)


person = {'name': 'Gman', 'age': 25}

person.get('name', 'unknown')   # 'Gman'
person.get('city', 'unknown')   # 'unknown' - no KeyError
person.get('age', 0)            # 25
'''
Plain English:
.get() returns the value if the key exists.
If the key doesn't exist it returns the fallback value instead of crashing with a KeyError.
Always use .get() when you're not sure if a key exists.

Use cases:
Looking up user data that might not exist
Counting word occurrences safely
Any dictionary lookup that could fail
'''

"4. .setdefault()"
_______.setdefault(_______, _______)


person = {'name': 'Gman'}

person.setdefault('age', 0)      # adds 'age': 0
person.setdefault('name', 'Bob') # does nothing - 'name' already exists
print(person)  # {'name': 'Gman', 'age': 0}
'''
Plain English:
Adds a key with a default value only if that key doesn't already exist.
If the key is already there it does nothing. Useful for initializing counters and default values safely.

Use cases:
Initializing a counter for a word that hasn't been seen yet
Setting default values without overwriting existing ones
'''


"5. Checking Keys and Values"
_______ in _______            # check if key exists
_______ in _______.keys()     # same as above
_______ in _______.values()   # check if value exists


person = {'name': 'Gman', 'age': 25}

'name' in person              # True - checks keys
'name' in person.keys()       # True - same thing
'Gman' in person.values()    # True - checks values
'city' in person              # False
'''
Plain English:
in on a dictionary checks keys by default.
To check values you must use .values() explicitly.
Knowing the difference prevents bugs when searching dictionaries.
Use cases:

Checking before accessing to avoid KeyErrors
Searching if a value exists anywhere in a dictionary
'''


"6. Nested Data Structures"
# List of dictionaries
_______ = [
    {_______: _______, _______: _______},
    {_______: _______, _______: _______}
]
_______[0][_______]   # access first item's key

# Dictionary of lists
_______ = {
    _______: [_______, _______],
    _______: [_______, _______]
}
_______[_______][0]   # access first item in a key's list


# List of dictionaries
students = [
    {'name': 'Gman', 'score': 92},
    {'name': 'Bob', 'score': 78}
]
students[0]['name']   # 'Gman'

# Dictionary of lists
grades = {
    'A': ['Gman', 'Jess'],
    'B': ['Sarah', 'Anna']
}
grades['A'][0]        # 'Gman'
grades['B'].append('Mike')
'''
Plain English:
Dictionaries and lists can contain each other.
A list of dictionaries is common for storing multiple records.
A dictionary of lists is common for grouping items by category.
Access by chaining the index and key together.

Use cases:
Student records, product catalogs, contact books
Grouping items by category like grades or tags
'''


"7. Pretty Printing"
import pprint
pprint.pprint(_______)

# Manual clean print
for _______, _______ in _______.items():
    print(f"{_______}: {_______}")


import pprint

person = {'name': 'Gman', 'age': 25, 'city': 'Windsor'}
pprint.pprint(person)

for key, value in person.items():
    print(f"{key}: {value}")
'''
Plain English:
pprint.pprint() formats dictionaries in a readable way automatically.
The manual loop gives you full control over how each key-value pair is displayed.

Use cases:
Debugging — checking what a dictionary contains
Displaying structured data cleanly to the user
'''

