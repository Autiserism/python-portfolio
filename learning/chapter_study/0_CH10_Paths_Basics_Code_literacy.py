Goal: Write a program that saves a message to a file.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 1 only:
In plain English: "I need to tell Python WHERE to save the file."

Which tool does that job?
A. Path()
B. write_text()
C. mkdir()
******************************************************************
A. Path()
//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('data') / 'message.txt'

"file_path points to a file called message.txt inside a folder called data"
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
You have a pointer. But the data folder might not exist yet.
In plain English: "I need to CREATE the folder before saving anything in it."

Which tool does that job?
A. file_path.write_text()
B. Path('data').mkdir(parents=True, exist_ok=True)
C. file_path.exists()
******************************************************************
B. Path('data').mkdir(parents=True, exist_ok=True)
//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('data') / 'message.txt'
Path('data').mkdir(parents=True, exist_ok=True)

"Create the data folder, create any missing parent folders, don't crash if it already exists"
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Folder exists. Pointer exists. Now actually save the message.
In plain English: "I need to WRITE text into the file."

Which tool does that job?
A. file_path.read_text()
B. file_path.exists()
C. file_path.write_text('Hello!')
******************************************************************
C. file_path.write_text('Hello!')
//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('data') / 'message.txt'
Path('data').mkdir(parents=True, exist_ok=True)
file_path.write_text('Hello!')

"Write the text Hello! into the file that file_path points to"
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
File is saved. Now confirm it worked.
In plain English: "I need to CHECK the file exists before trying to read it back."

Which tool does that job?
A. file_path.mkdir()
B. file_path.exists()
C. file_path.write_text()
******************************************************************
B. file_path.exists()
//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('data') / 'message.txt'
Path('data').mkdir(parents=True, exist_ok=True)
file_path.write_text('Hello!')

if file_path.exists():
    print('file saved successfully')

"If the file exists at that location, print success"
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Final step. Actually read the saved message back and print it.
In plain English: "I need to READ the text from the file."

Which tool does that job?
A. file_path.read_text()
B. file_path.glob()
C. file_path.suffix
******************************************************************
A. file_path.read_text()
//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('data') / 'message.txt'
Path('data').mkdir(parents=True, exist_ok=True)
file_path.write_text('Hello!')

if file_path.exists():
    print print('file saved successfully')
    contents = file_path.read_text()
    print(contents)

You just built a complete save/load program in 5 steps!
Each step had ONE job:

Path() - point to location
.mkdir() - create folder
.write_text() - save file
.exists() - verify it worked
.read_text() - read it back

This is the assembly pattern for almost every file program:
Point → Create folder → Write → Verify → Read
New tools needed: json.dumps() and json.loads()
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 2.
Step 1 only:
You have this data:
names = ['John', 'Jane', 'Bob']
In plain English: "I need to tell Python WHERE to save the file."
Write the two lines needed - import and pointer.
//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('people') / 'names.json'
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Why it matters:
'names.txt'   # Works but misleading - txt implies plain text
'names.json'  # Correct - tells anyone reading the code what's inside
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
In plain English: "I need to CREATE the folder before saving."
Write that one line.

//////////////////////////////////////////////////////////////////
from pathlib import Path

file_path = Path('people') / 'names.json'
Path('people').mkdir(parents=True, exist_ok=True)                <
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
You have this data:
names = ['John', 'Jane', 'Bob']
write_text() only saves strings. A list is NOT a string.
In plain English: "I need to CONVERT the list to a string before saving."
Which tool does that?
A. str(names)
B. json.dumps(names)
C. names.write_text()
******************************************************************
B. json.dumps(names)
------------------------------------------------------------------
its json.dumps() with an s:
json.dump(names)   # Writes to a file object (different use)
json.dumps(names)  # Converts to string (what we need here)
Memory trick:

json.dumps() = dump to string
json.dump() = dump to file object

Write the two lines - import json and save the file:
import json
file_path.write_text(json.dumps(names))
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json                                                      <

names = ['John', 'Jane', 'Bob']

file_path = Path('people') / 'names.json'
Path('people').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(names))                          <
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
In plain English: "I need to READ the file back and CONVERT the string back to a list."
Two tools needed together - which pair?
A. read_text() and json.loads()
B. read_bytes() and json.dump()
C. write_text() and json.dumps()
******************************************************************
A. read_text() and json.loads()
------------------------------------------------------------------
Write those two lines:
# Hint: read the file first, then convert
content = ___
loaded_names = ___
******************************************************************
content = file_path.read_text()
loaded_names = json.loads(content)
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

names = ['John', 'Jane', 'Bob']

file_path = Path('people') / 'names.json'
Path('people').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(names))
content = file_path.read_text()                                  <
loaded_names = json.loads(content)                               <
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
In plain English: "Check the file exists then print each loaded name."
Write those lines:

if ___:
    for name in ___:
        print(___)
******************************************************************
if file_path.exists():
    for name in loaded_names:
        print(name)
//////////////////////////////////////////////////////////////////
from pathlib import path
import json

names = ['John', 'Jane', 'Bob']

file_path = Path('people') / 'names.json'
Path('people').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(names))
content = file_path.read_text()
loaded_names = json.loads(content)

if file_path.exists():                                           <
    for name in loaded_names:                                    <
        print(name)                                              <
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
The pattern is the same as Program 1:
Point → Create folder → Convert + Write → Verify → Read + Convert back
New tools added:

json.dumps(list)    # list → string (before saving)
json.loads(string)  # string → list (after loading)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 3 - Save a contact dictionary to JSON, load it back, access specific values.

Goal: Save one contact to a JSON file, load it back, print just the name and phone.

You have this data:

contact = {
    'name': 'John Smith',
    'phone': '416-555-1234',
    'email': 'john@email.com'
}

Step 1 only:
Write the imports and pointer. File called contact.json inside folder contacts.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

file_path = Path('contacts') / 'contact.json'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Create the folder safely.

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('contacts') / 'contacts.json'

Path('contacts').mkdir(parents=True, exist_ok=True)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Save the contact dictionary to the file.

contact = {
    'name': 'John Smith',
    'phone': '416-555-1234',
    'email': 'john@email.com'
}

Write the one line that converts and saves it.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('contacts') / 'contacts.json'
Path('contacts').mkdir(parents=True, exist_ok=True)

file_path.write_text(json.dumps(contact))
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Load the file back. Two lines - read the file, convert string back to dictionary.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('contacts') / 'contacts.json'
Path('contacts').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(contact))

content = file_path.read_text()
load_contacts = json.loads(content)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Final step. Check file exists, then print ONLY the name and phone from the loaded dictionary.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

contact = {
    'name': 'John Smith',
    'phone': '416-555-1234',
    'email': 'john@email.com'
}

file_path = Path('contacts') / 'contacts.json'
Path('contacts').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(contact))

content = file_path.read_text()
loaded_contact = json.loads(content)

if file_path.exists():
    print(f"Name: {loaded_contact['name']}")
    print(f"Phone: {loaded_contact['phone']}")
******************************************************************
#Output:
Name: John Smith
Phone: 416-555-1234
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
load_contacts = json.load(content)   # Wrong - load() reads from file object
load_contacts = json.loads(content)  # Correct - loads() reads from string

json.load vs json.loads - burn this in:

json.dumps(data)      # dict/list → string (s = string)
json.loads(string)    # string → dict/list (s = string)

json.dump(data, file) # dict/list → file object
json.load(file)       # file object → dict/list
Youll use dumps and loads most often.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 4 - Save multiple contacts, load them back, search by name.
Goal: Save a list of contact dictionaries to JSON, load them back, find a specific contact by name.

You have this data:
contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]
Step 1 only:
Write imports and pointer. File called contacts.json inside folder data.

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Create the folder safely.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'

Path('data').mkdir(parents=True, exist_ok=True)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Save the contacts list to the file.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)

file_path.write_text(json.dumps(contacts))
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Load the file back into a variable called loaded_contacts.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(contacts))
contents = file_path.read_text()
load_contacts = json.loads(contents)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Search the loaded contacts by name. Find and print the contact named 'Jane Doe'.

search = 'Jane Doe'

for contact in ___:
    if contact[___] == ___:
        print(___)

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(contacts))
contents = file_path.read_text()
load_contacts = json.loads(contents)

for contact in load_contacts:
    if contact['name'] == search:
        print(contact)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Complete program - type it all out and run it:

from pathlib import Path
import json

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)
file_path.write_text(json.dumps(contacts))

contents = file_path.read_text()
loaded_contacts = json.loads(contents)

search = 'Jane Doe'
for contact in loaded_contacts:
    if contact['name'] == search:
        print(contact)
******************************************************************
Output:
{'name': 'Jane Doe', 'phone': '647-555-5678'}
//////////////////////////////////////////////////////////////////
Pattern recognition - you have now written this 4 times:
# Save
file_path.write_text(json.dumps(data))

# Load
contents = file_path.read_text()
data = json.loads(contents)
That pair should be starting to feel automatic.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 5 - Same program, wrapped in functions.

Goal: Same save/load/search logic but organized into reusable functions.

You have the same data:

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]
Step 1 only:
Write imports, pointer, and folder creation. Same as before.

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Write a function called save_contacts that takes contacts and file_path as parameters and saves the list to JSON.

def save_contacts(___,  ___):
    ___

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)

def save_contacts(contacts, file_path):
    file_path.write_text(json.dumps(contacts))
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Write a function called load_contacts that takes file_path as parameter,
checks the file exists, loads and returns the contacts. Returns empty list if file not found.

def load_contacts(___):
    if ___:
        ___
        return ___
    return ___

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)

def save_contacts(contacts, file_path):
    file_path.write_text(json.dumps(contacts))

def load_contacts(file_path):
    if file_path.exists():
        contents = file_path.read_text()
        data = json.loads(contents)
        return load_contacts
    return []
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Write a function called search_contacts that takes contacts and name as parameters and returns the matching contact or None if not found.

def search_contacts(___, ___):
    for contact in ___:
        if ___:
            return ___
    return ___

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)

def save_contacts(contacts, file_path):
    file_path.write_text(json.dumps(contacts))

def load_contacts(file_path):
    if file_path.exists():
        contents = file_path.read_text()
        data = json.loads(contents)
        return data
    return []

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Call all three functions together:

Save contacts
Load them back
Search for 'Jane Doe'
Print result if found, 'Not found' if not

___  # save
___  # load
___  # search

if ___:
    print(___)
else:
    print('Not found')

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

file_path = Path('data') / 'contacts.json'
Path('data').mkdir(parents=True, exist_ok=True)

def save_contacts(contacts, file_path):
    file_path.write_text(json.dumps(contacts))

def load_contacts(file_path):
    if file_path.exists():
        contents = file_path.read_text()
        data = json.loads(contents)
        return data
    return []

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

save_contacts(contacts, file_path)
loaded = load_contacts(file_path)
result = search_contacts(loaded, 'Jane Doe')

if result:
    print(f"Name: {result['name']} Phone: {result['phone']}")
else:
    print('Not found')
******************************************************************
Three patterns to burn in:
# Always save function return values
loaded = load_contacts(file_path)    # ✓ save it
result = search_contacts(loaded, name)  # ✓ save it

# Variables inside functions stay inside functions
def my_func():
    x = 10  # only exists inside here

# mkdir needs the folder name
Path('data').mkdir()  # ✓ always needs the name
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 6 - Save and load contacts using shelve.

Goal: Same contacts, same save/load/search functions but using shelve instead of JSON.
Key difference from JSON:
# JSON - convert to string first
file_path.write_text(json.dumps(contacts))

# shelve - saves Python objects directly
shelf['contacts'] = contacts  # No converting needed!

You have the same data:

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]
Step 1 only:

Write imports, folder creation, and shelf path pointer.
# Hint: shelve needs str() conversion
# Shelf file called 'contacts_shelf' inside 'data'

//////////////////////////////////////////////////////////////////
from pathlib import Path
import shelve
file_path = Path('data')
file_path.mkdir(parents=True,exist_ok=True)

shelf_path = file_path / 'contacts_shelf'
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Write a function called save_contacts that takes contacts and shelf_path as parameters and saves to shelve.
def save_contacts(___, ___):
    with shelve.open(___) as shelf:
        shelf[___] = ___

//////////////////////////////////////////////////////////////////
from pathlib import Path
import shelve

file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
shelf_path = file_path / 'contacts_shelf'

def save_contacts(contacts, shelf_path):
    with shelve.open(str(shelf_path)) as shelf: # str(shelf_path) Is Critical
        shelf['contacts'] = contacts

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Write load_contacts function that takes shelf_path, loads and returns contacts.
Returns empty list if key doesnt exist.

def load_contacts(___):
    with shelve.open(___) as shelf:
        return shelf.___(___,  ___)
//////////////////////////////////////////////////////////////////
from pathlib import Path
import shelve

file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
shelf_path = file_path / 'contacts_shelf'

def save_contacts(contacts, shelf_path):
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts        # shelf not shelf_path

def load_contacts(shelf_path):
    with shelve.open(str(shelf_path)) as shelf:
        return shelf.get('contacts', [])    # 'contacts' in quotes
******************************************************************
Rule to burn in:
with shelve.open(str(shelf_path)) as shelf:
#                   ^^^^^^^^^^^       ^^^^
#                   file location     dictionary to use
#                   (Path → string)   (use this, not shelf_path!)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:

Write search_contacts - same as Program 5, takes contacts and name, returns match or None.

//////////////////////////////////////////////////////////////////
from pathlib import Path
import shelve
file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
shelf_path = file_path / 'contacts_shelf'


def save_contacts(shelf_path, contacts):
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts

def load_contacts (shelf_path):
    with shelve.open(str(shelf_path)) as shelf:
        return shelf.get('contacts', [])

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Call all three functions - save, load, search for 'John Smith', print result.

//////////////////////////////////////////////////////////////////
from pathlib import Path
import shelve

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
shelf_path = file_path / 'contacts_shelf'

def save_contacts(contacts, shelf_path):
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts

def load_contacts(shelf_path):
    with shelve.open(str(shelf_path)) as shelf:
        return shelf.get('contacts', [])

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

save_contacts(contacts, shelf_path)
loaded = load_contacts(shelf_path)
result = search_contacts(loaded, 'John Smith')

if result:
    print(f"Name: {result['name']} Phone: {result['phone']}")
else:
    print('Not found')


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 7 - Save to JSON and backup to shelve.

Goal: Save contacts to JSON as main storage, shelve as backup. Load from JSON, fall back to shelve if JSON missing.

Step 1 only:
Write imports, folder creation, both file pointers.

# Need: pathlib, json, shelve
# JSON file: 'contacts.json' inside 'data'
# Shelf file: 'contacts_backup' inside 'data'

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json, shelve

file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
json_path = file_path / 'contacts.json'
shelf_path = file_path / 'contacts_backup'
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Write save_contacts that saves to BOTH JSON and shelve.

def save_contacts(contacts, json_path, shelf_path):
    # Save to JSON
    ___
    # Save to shelve
    with shelve.open(___) as shelf:
        ___

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json, shelve
file_path = Path('data')
file_path.mkdir(parents=True,exist_ok=True)
json_path = file_path / 'contacts.json'
shelf_path = file_path / 'contacts_shelf'

def save_contacts(contacts, json_path, shelf_path):
    json_path.write_text(json.dumps(contacts))
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Write load_contacts that:

Tries JSON first
Falls back to shelve if JSON missing
Returns empty list if both missing

def load_contacts(json_path, shelf_path):
    if ___:
        contents = ___
        return ___
    else:
        with shelve.open(___) as shelf:
            return shelf.get(___, ___)

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json, shelve
file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
json_path = file_path / 'contacts.json'
shelf_path = file_path / 'contacts_shelf'
def save_contacts(contacts, json_path, shelf_path):
    json_path.write_text(json.dumps(contacts))
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts

def load_contacts(json_path, shelf_path):
    if json_path.exists():
        contents = json_path.read_text()
        return json.loads(contents)
    else:
        with shelve.open(str(shelf_path)) as shelf:
            return shelf.get('contacts', [])
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Write search_contacts - same as every previous program.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json, shelve
file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
json_path = file_path / 'contacts.json'
shelf_path = file_path / 'contacts_shelf'
def save_contacts(contacts, json_path, shelf_path):
    json_path.write_text(json.dumps(contacts))
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts
def load_contacts(json_path, shelf_path):
    if json_path.exists():
        content = json_path.read_text()
        return json.loads(content)
    else:
        with shelve.open(str(shelf_path)) as shelf:
            return shelf.get('contacts', [])

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Call everything:

Save contacts
Load contacts
Search for 'Jane Doe'
Print name and phone if found, 'Not found' if not
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json, shelve

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]
file_path = Path('data')
file_path.mkdir(parents=True, exist_ok=True)
json_path = file_path / 'contacts.json'
shelf_path = file_path / 'contacts_shelf'

def save_contacts(contacts, json_path, shelf_path):
    json_path.write_text(json.dumps(contacts))
    with shelve.open(str(shelf_path)) as shelf:
        shelf['contacts'] = contacts

def load_contacts(json_path, shelf_path):
    if json_path.exists():
        content = json_path.read_text()
        return json.loads(content)
    else:
        with shelve.open(str(shelf_path)) as shelf:
            return shelf.get('contacts', [])

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

save_contacts(contacts, json_path, shelf_path)
loaded = load_contacts(json_path, shelf_path)
result = search_contacts(loaded, 'Jane Doe')

if result:
    print(f"Name: {result['name']} Phone: {result['phone']}")
else:
    print('Not found')
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 8 - Find all JSON files in a folder and load them all.

Goal: Scan a folder for all .json files, load each one, print contents.

Step 1 only:
Write imports and pointer to folder called data.
//////////////////////////////////////////////////////////////////
#This program scans for existing files - no need to create a specific file pointer yet:
from pathlib import Path
import json

data_dir = Path('data')
------------------------------------------------------------------
No mkdir needed either - were reading existing files, not creating new ones.
Note: Changed file_path to data_dir -
more descriptive when pointing to a folder well search through.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Find all .json files inside data_dir and store as a list.
json_files = ___
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

data_dir = Path('data')
json_files = list(data_dir.glob('*.json')) #wrap in list() so you can reuse it:
------------------------------------------------------------------
Why list():
# Without list() - generator (can only loop once)
json_files = data_dir.glob('*.json')

# With list() - reusable
json_files = list(data_dir.glob('*.json'))
print(f'Found {len(json_files)} files')  # len() needs a list
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Print how many JSON files were found.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')
json_files = list(data_dir.glob('*.json'))

print(f"found {len(json_files)}, .json files ")
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Loop through each file, check its actually a file, read and print its contents.

for file in ___:
    if ___:
        content = ___
        print(f'___ : ___')
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

data_dir = Path('data')
json_files = list(data_dir.glob('*.json'))

print(f'Found {len(json_files)} json files')

for file in json_files:
    if file.exists() and file.is_file():
        content = file.read_text()
        data = json.loads(content)
        print(f'{file.name}: {data}')
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 9 - Glob finds files, load each one, search across all of them.

Goal: Scan folder for all JSON files, load each one, search all contacts across all files for a name.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 1 only:
Write imports and folder pointer. No mkdir - reading existing files.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Find all JSON files and store as a list.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')

json_files = list(data_dir.glob('*.json'))
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Write a function called load_all_contacts that:

Takes json_files as parameter
Creates empty list called all_contacts
Loops through each file
Checks its a valid file
Loads contents and adds to all_contacts
Returns all_contacts

def load_all_contacts(___):
    all_contacts = ___
    for file in ___:
        if ___ and ___:
            content = ___
            data = ___
            all_contacts.___(data)
    return ___
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')
json_files = list(data_dir.glob('*.json'))

def load_all_contacts(json_files):
    all_contacts = []
    for file in json_files:
        if file.exists() and file.is_file():
            content = file.read_text()
            data = json.loads(content)
            all_contacts.append(data)
    return all_contacts
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Write search_contacts - takes all_contacts and name, searches and returns match or None.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')
json_files = list(data_dir.glob('*.json'))

def load_all_contacts(json_files):
    all_contacts = []
    for file in json_files:
        if file.exists() and file.is_file():
            contents = file.read_text()
            data = json.loads(contents)
            all_contacts.append(data)
    return all_contacts

def search_contacts(all_contacts, name):
    for contact in all_contacts:
        if contact['name'] == name:
        return contact
    return None
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Call everything together:

Load all contacts
Search for 'John Smith'
Print result or 'Not found'
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

data_dir = Path('data')
json_files = list(data_dir.glob('*.json'))

def load_all_contacts(json_files):
    all_contacts = []
    for file in json_files:
        if file.exists() and file.is_file():
            contents = file.read_text()
            data = json.loads(contents)
            all_contacts.append(data)
    return all_contacts

def search_contacts(all_contacts, name):
    for contact in all_contacts:
        if contact['name'] == name:
            return contact        # ✓ indented under if
    return None

all_contacts = load_all_contacts(json_files)
result = search_contacts(all_contacts, 'John Smith')

if result:
    print(f"Name: {result['name']} Phone: {result['phone']}")
else:
    print('Not found')
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'Program 10 - Full mini-program. Multiple JSON files, glob finds them, load and search.

Goal: Save three contacts each as their OWN JSON file, glob finds all of them, load and search by name.

You have this data:

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

Each contact gets its own file:
data/John_Smith.json
data/Jane_Doe.json
data/Bob_Wilson.json
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 1 only:
Write imports and folder creation.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 2 only:
Write a function save_contact that takes ONE contact and data_dir, saves it to its own JSON file named after the contact.

Hint: Replace spaces in name with underscores for filename. # 'John Smith' → 'John_Smith.json'
filename = contact['name'].replace(' ', '_') + '.json'

Write the complete function:

def save_contact(contact, data_dir):
    filename = ___
    file_path = ___
    file_path.___
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

def save_contact(contact, data_dir):
    filename = contact['name'].replace(' ', '_') + '.json'
    file_path = data_dir / filename
    file_path.write_text(json.dumps(contact))
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 3 only:
Loop through all contacts and call save_contact for each one.

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

for ___ in ___:
    ___

//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

def save_contact(contact, data_dir):
    filename = contact['name'].replace(' ', '_') + '.json'
    file_path = data_dir / filename
    file_path.write_text(json.dumps(contact))

for contact in contacts:
    save_contact(contact, data_dir)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 4 only:
Write load_all_contacts - glob finds all JSON files, loads each one, returns list of all contacts.
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json
data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)
def save_contact(contact, data_dir):
    filename = contact['name'].replace(' ', '_') + '.json'
    file_path = data_dir / filename
    file_path.write_text(json.dumps(contact))
for contact in contacts:
    save_contact(contact, data_dir)

#def load_all_contacts():              # ✗ no parameter - relies on global variable
def load_all_contacts(data_dir):       # ✓ pass data_dir in
    json_files = list(data_dir.glob('*.json'))
    all_contacts = []
    for file in json_files:
        if file.exists() and file.is_file():
            contents = file.read_text()
            data = json.loads(contents)
            all_contacts.append(data)
    return all_contacts
******************************************************************
# Without parameter - only works for ONE folder (global)
def load_all_contacts():
    json_files = list(data_dir.glob('*.json'))  # hardcoded

# With parameter - works for ANY folder
def load_all_contacts(data_dir):
    json_files = list(data_dir.glob('*.json'))  # flexible
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Step 5 only:
Write search_contacts and call everything together:

Save all contacts
Load all contacts
Search for 'Jane Doe'
Print result or 'Not found'
//////////////////////////////////////////////////////////////////
from pathlib import Path
import json

contacts = [
    {'name': 'John Smith', 'phone': '416-555-1234'},
    {'name': 'Jane Doe', 'phone': '647-555-5678'},
    {'name': 'Bob Wilson', 'phone': '519-555-9999'}
]

data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

def save_contact(contact, data_dir):
    filename = contact['name'].replace(' ', '_') + '.json'
    file_path = data_dir / filename
    file_path.write_text(json.dumps(contact))

def load_all_contacts(data_dir):
    json_files = list(data_dir.glob('*.json'))
    all_contacts = []
    for file in json_files:
        if file.exists() and file.is_file():
            contents = file.read_text()
            data = json.loads(contents)
            all_contacts.append(data)
    return all_contacts

def search_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

for contact in contacts:
    save_contact(contact, data_dir)

loaded = load_all_contacts(data_dir)
result = search_contacts(loaded, 'Jane Doe')

if result:
    print(f"Name: {result['name']} Phone: {result['phone']}")
else:
    print('Not found')
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
built from scratch 10 times:

# The core pattern
Path('folder').mkdir(parents=True, exist_ok=True)  # Create folder
file_path = Path('folder') / 'file.json'           # Point to file
file_path.write_text(json.dumps(data))             # Save
contents = file_path.read_text()                   # Load
data = json.loads(contents)                        # Convert

# Shelve pattern
with shelve.open(str(shelf_path)) as shelf:
    shelf['key'] = data          # Save
    data = shelf.get('key', [])  # Load

# Glob pattern
files = list(Path('folder').glob('*.json'))
for file in files:
    if file.is_file():
        data = json.loads(file.read_text())

Consistent mistakes to keep watching:

pathlib not pathlin
file_path.read_text() not read_text()
json.loads() not json.load()
== not = in comparisons
str(shelf_path) for shelve
Singular vs plural parameter names

//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


//////////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



















