    Practice Exercises - Level 1
One concept at a time. Fill in the blanks.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Exercise 1 - Point to a file

from pathlib import Path

# Point to a file called 'notes.txt' inside a folder called 'documents'
file_path = ___

//////////////////////////////////////////////////////////////////
# Wrong - / inside quotes is just a string
file_path = Path('documents'/'notes.txt')

# Correct - / operator between two Path/string pieces
file_path = Path('documents') / 'notes.txt'
Rule: The / operator works between Path objects and strings, not inside a string.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Exercise 2 - Create a folder

from pathlib import Path

# Create a folder called 'logs' inside 'data'
# Make sure it works even if 'data' doesn't exist yet
# Make sure it doesn't crash if 'logs' already exists

folder = Path('data') / 'logs'
folder.___(___, ___)

//////////////////////////////////////////////////////////////////
# Wrong - dot in wrong place
folder.mkdir.(parents=True, exist_ok=True)
            ^


# Correct
folder.mkdir(parents=True, exist_ok=True)
Rule: Method calls are always object.method(arguments) - no dot before the brackets.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Exercise 3 - Check before reading

from pathlib import Path

file_path = Path('data') / 'contacts.json'

# Only read the file if it exists AND is a file
if ___ and ___:
    content = ___
    print(content)

//////////////////////////////////////////////////////////////////
Where/why: Any time you read a file in a real program -
always guard with exists() and is_file() first.
Skipping this crashes your program if the file was deleted, moved, or never created.

from pathlib import Path

file_path = Path('data') / 'contacts.json'

if file_path.exists() and file_path.is_file():
    content = file_path.read_text()
    print(content)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Exercise 4 - Write to a file
Where/why: Saving program output, user data, or logs to disk so it survives after the program closes.

from pathlib import Path

output_dir = Path('output')
output_dir.mkdir(parents=True, exist_ok=True)

file_path = output_dir / 'results.txt'

# Write 'Program complete!' to the file
___

//////////////////////////////////////////////////////////////////

file_path.write_text('Program complete!')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Exercise 5 - Find files by pattern
Where/why: Searching a folder for specific file types - like finding all log files to analyze or all JSON files to process.

from pathlib import Path

data_dir = Path('data')

# Find all .txt files in data_dir
# Store as a list
# Print how many were found

txt_files = ___
print(___)

//////////////////////////////////////////////////////////////////

txt_files = [f for f in data_dir.glob('*.txt') if f.is_file()]
print(f'Found {len(txt_files)} txt files')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Level 2 - Two Concepts Combined

Exercise 6 - Create folder then save file
Where/why: Standard pattern for any program that saves output -
create the destination folder first, then write the file.
Used in W3P3 (log analyzer), W3P5 (address book), any data-saving program.

from pathlib import Path

# 1. Create folder 'reports/2024' (safe - no errors if exists)
# 2. Point to a file 'summary.txt' inside it
# 3. Write 'Report complete' to the file

reports_dir = ___
reports_dir.___
file_path = ___
file_path.___

//////////////////////////////////////////////////////////////////

reports_dir = Path('reports/2024')
reports_dir.mkdir(parents=True, exist_ok=True)
file_path = reports_dir / 'summary.txt'
file_path.write_text('Report complete')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Exercise 7 - Read file, check extension first
Where/why: Processing files from user input or unknown sources -
always verify you have the right file type before trying to read it.
Prevents errors when users accidentally select wrong files.

from pathlib import Path

file_path = Path('data/contacts.json')

# 1. Check file exists AND is a .json file
# 2. If yes, read and print contents
# 3. If no, print 'Not a valid JSON file'

if ___ and ___:
    ___
else:
    ___

//////////////////////////////////////////////////////////////////
# Wrong - glob searches directories, not checks file type
if file_path.exists() and file_path.glob('*.json'):

# Correct - suffix checks the extension
if file_path.exists() and file_path.suffix == '.json':
    content = file_path.read_text()
    print(content)
else:
    print('Not a valid JSON file')

Rule:

glob() = search a folder for matching files
.suffix = check a single files extension

When to use each:

# glob - finding files in a folder
Path('data').glob('*.json')      # Find all json files in data/

# suffix - checking one specific file
file_path.suffix == '.json'      # Is this file a json?
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Exercise 8 - shelve save and load
Where/why: Saving program state between sessions -
like W3P5 contacts surviving after the program closes and reloading automatically next run.

from pathlib import Path
import shelve

data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

contacts = [{'name': 'John'}, {'name': 'Jane'}]

# 1. Save contacts to shelve file called 'contacts_shelf' inside data_dir
# 2. Load them back into a new variable called 'loaded'
# 3. Print loaded

shelf_path = ___
with shelve.open(___) as shelf:
    shelf[___] = ___

with shelve.open(___) as shelf:
    loaded = ___
print(loaded)

//////////////////////////////////////////////////////////////////
shelve.open() needs a string, not a Path object:

# Wrong - shelve doesn't accept Path objects
with shelve.open(shelf_path) as shelf:

# Correct - convert Path to string
with shelve.open(str(shelf_path)) as shelf:
Complete correct version:

shelf_path = data_dir / 'contacts_shelf'

with shelve.open(str(shelf_path)) as shelf:
    shelf['contacts'] = [{'name': 'John'}, {'name': 'Jane'}]

with shelve.open(str(shelf_path)) as shelf:
    loaded = shelf.get('contacts', [])

print(loaded)

Two corrections:

str(shelf_path) - convert Path to string
shelf.get('contacts', []) - safer than direct access

Rule to remember:

# Path objects work with most things
file_path.write_text()     # ✓ Path object fine
file_path.read_text()      # ✓ Path object fine
open(file_path, 'a')       # ✓ Path object fine

# shelve is the exception
shelve.open(str(path))     # ✗ Must convert to string!
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Exercise 9 - Find files and list their names
Where/why: Building file browsers, processing batches of files,
generating reports of what exists in a folder. Used whenever you need to inventory or process multiple files.

from pathlib import Path

project_dir = Path('myproject')

# 1. Find all .py files recursively (all subfolders)
# 2. Print each file's name and parent folder

for file in ___:
    print(f'File: ___  Location: ___')

//////////////////////////////////////////////////////////////////
file already has the full path - use .name and .parent for cleaner output:
# Works but prints full path and wrong location
for file in project_dir.glob('**/*.py'):
    print(f'File: {file}  Location: {project_dir}')
# File: myproject/utils/helper.py  Location: myproject

# Better - specific attributes for cleaner output
for file in project_dir.glob('**/*.py'):
    print(f'File: {file.name}  Location: {file.parent}')
# File: helper.py  Location: myproject/utils
# File: main.py    Location: myproject
Why .parent over project_dir:

project_dir = always just myproject (top level)
file.parent = exact folder containing THAT file (could be any subfolder)

Attributes on each result:

for file in project_dir.glob('**/*.py'):
    file.name    # 'helper.py'
    file.stem    # 'helper'
    file.suffix  # '.py'
    file.parent  # Path('myproject/utils')
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Exercise 10 - os.path check then rename
Where/why: Renaming files safely during processing - like adding timestamps to log files or creating backups before overwriting.

import os

old_name = 'data/report.txt'
new_name = 'data/report_backup.txt'

# 1. Check old file exists
# 2. Check new name doesn't already exist (don't overwrite backup!)
# 3. If both conditions met, rename and print success
# 4. Otherwise print why it failed

if ___ and ___:
    ___
    print('renamed!')
elif ___:
    print('original file not found')
else:
    print('backup already exists')

//////////////////////////////////////////////////////////////////
if old_name.exists() and old_name.is_file():
    if not old_name.exists():
        old_name.mkdir()
elif not old_name.exists():
   print('original file not found')
else:
    print('backup already exists')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
if os.path.exists(old_name) and not os.path.exists(new_name):
    os.rename(old_name, new_name)
    print('renamed!')
elif not os.path.exists(old_name):
    print('original file not found')
else:
    print('backup already exists')
Key corrections:

os.path.exists(string) not string.exists()
.exists() only works on Path objects
Use os.rename() not mkdir() (that creates folders!)
Check not os.path.exists(new_name) to avoid overwriting

Rule to remember:
python# String - needs os.path
old_name = 'data/report.txt'
os.path.exists(old_name)     # ✓

# Path object - has its own methods
p = Path('data/report.txt')
p.exists()                   # ✓

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









