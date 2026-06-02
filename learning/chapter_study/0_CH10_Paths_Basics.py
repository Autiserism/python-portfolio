  File Operations - Basics

os + Path + glob Summary

import os
import glob
from pathlib import Path

# Location
os.getcwd()              # Where am I? (string)
Path.cwd()               # Where am I? (Path)

# Contents
os.listdir('.')          # What's here? (strings)
Path('.').iterdir()      # What's here? (Path objects)
Path('.').glob('*.txt')  # What .txt files are here?

# Path info
os.path.basename(p)      # Filename
os.path.dirname(p)       # Folder
os.path.splitext(p)      # ('name', '.ext')

Path(p).name             # Filename
Path(p).parent           # Folder
Path(p).stem             # Name without extension
Path(p).suffix           # Extension

# Checks
os.path.exists(p)        # Exists?
os.path.isfile(p)        # Is file?
os.path.isdir(p)         # Is folder?
Path(p).exists()
Path(p).is_file()
Path(p).is_dir()

# File operations
Path(p).read_text()      # Read
Path(p).write_text()     # Write
os.rename(old, new)      # Rename
os.remove(p)             # Delete
//////////////////////////////////////////////////////////////////

    10 Concepts Drilled - Summary

from pathlib import Path
import shelve, json

# 1. Point to locations
data_dir = Path('data')
file_path = data_dir / 'contacts.json'

# 2. Create folder
data_dir.mkdir(parents=True, exist_ok=True)

# 3. Check what's there
file_path.exists()   # exists at all?
file_path.is_file()  # is it a file?
file_path.is_dir()   # is it a folder?

# 4. Read/Write files
content = file_path.read_text()       # get string
file_path.write_text('string here')   # save string (overwrites)

# 5. shelve (Python objects)
with shelve.open('storage') as shelf:
    shelf['key'] = any_python_object       # save
    data = shelf.get('key', default_val)   # load safely

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 1: What is a Path Object?

Plain English:
A Path object is Pythons way of representing a file or folder location.
Its smarter than a plain string because it understands folders, filenames, and works on any operating system.

from pathlib import Path

# Without Path (just a string - dumb)
file = 'data/contacts.json'

# With Path (smart object with useful tools)
file = Path('data/contacts.json')

    Question 1: In plain English, what is this line doing and why?
from pathlib import Path

//////////////////////////////////////////////////////////////////

pathlib is the module (the library), Path is the specific tool inside it we need.

import pathlib           # Gets the whole module
pathlib.Path('data')     # Have to reference module each time

from pathlib import Path  # Grabs just Path directly
Path('data')              # Cleaner to use

Both work, second is cleaner.
And yes - import Path alone would error because Python doesnt know which module to find it in.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 2: In plain English, what is this line doing and why?

data_dir = Path('data')

//////////////////////////////////////////////////////////////////

data_dir now holds a Path object pointing to a folder called 'data'.

Important distinction:

data_dir = Path('data')
This does NOT create the folder yet. It just creates a pointer to where it would be -
like writing an address on paper before the house is built.

# Just a pointer (no folder created yet)
data_dir = Path('data')

# NOW create the actual folder
data_dir.mkdir()

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 3: In plain English, what is each line doing and why?

data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

//////////////////////////////////////////////////////////////////
parents=True means "create ALL folders along the way if they don't exist yet"
# Without parents=True

Path('data/logs/2024').mkdir()
# FAILS if 'data' or 'logs' don't exist yet

# With parents=True
Path('data/logs/2024').mkdir(parents=True)
# Creates 'data', then 'logs', then '2024' automatically

exist_ok=True means "don't crash if folder already exists"

# Without exist_ok=True
Path('data').mkdir()  # Run twice = ERROR (folder exists!)

# With exist_ok=True
Path('data').mkdir(exist_ok=True)  # Run twice = fine

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 4: In plain English, what does each line do and why?

data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)
file_path = data_dir / 'contacts.json'

//////////////////////////////////////////////////////////////////
The / operator builds a path:

data_dir = Path('data')           # Points to: data/
file_path = data_dir / 'contacts.json'  # Points to: data/contacts.json
Three steps to remember:
 # Step 1: Point to folder
data_dir = Path('data')

# Step 2: Create the folder
data_dir.mkdir(parents=True, exist_ok=True)

# Step 3: Point to file inside folder
file_path = data_dir / 'contacts.json'

# Step 4: NOW create/write the file
file_path.write_text('hello')  # File finally exists!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 5: In plain English, what does each line do and why?

file_path = Path('data/contacts.json')

if file_path.exists():
    print('file found')
else:
    print('file not found')

//////////////////////////////////////////////////////////////////
Plain English:
Check if a file or folder actually exists at that location before trying to use it.
Trying to read a file that doesnt exist crashes your program.

file_path = Path('data/contacts.json')

if file_path.exists():
    print('file found')
else:
    print('file not found')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 6: In plain English, what does each line do and why?

Plain English hint: After confirming something exists, you might want to know what TYPE of thing it is.
file_path = Path('data/contacts.json')
folder_path = Path('data')

print(file_path.is_file())   # ???
print(folder_path.is_dir())  # ???
print(file_path.is_dir())    # ???

//////////////////////////////////////////////////////////////////
Plain English:
is_file() and is_dir() tell you what TYPE the path points to.
Useful when you need different behavior depending on whether its a file or folder.

file_path = Path('data/contacts.json')
folder_path = Path('data')

print(file_path.is_file())   # True  - it's a file
print(folder_path.is_dir())  # True  - it's a directory
print(file_path.is_dir())    # False - file is not a directory

Common real use:
path = Path('data')

if path.exists():
    if path.is_file():
        print('reading file...')
    elif path.is_dir():
        print('looking inside folder...')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 7: In plain English, what does each line do and why?

Plain English hint: Once you know a file exists, you want to actually get whats inside it.

file_path = Path('data/contacts.json')

content = file_path.read_text()
print(content)

//////////////////////////////////////////////////////////////////
Plain English:
read_text() opens the file, reads everything inside as a string, then closes it automatically.
The string is stored in your variable to use in your program.

file_path = Path('data/contacts.json')

content = file_path.read_text()
print(content)

Important: content is just a plain string at this point:

content = file_path.read_text()
print(type(content))  # <class 'str'>
print(content)        # '{"name": "John", "phone": "555-1234"}'

To actually USE the data (convert string to Python object):
import json

content = file_path.read_text()   # String
data = json.loads(content)        # Python dict/list

print(type(data))   # <class 'dict'>
print(data['name']) # 'John'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 8: In plain English, what does each line do and why?
Plain English hint: The opposite of reading - putting content INTO a file.

file_path = Path('data/notes.txt')

file_path.write_text('Hello World')

//////////////////////////////////////////////////////////////////
Plain English:
write_text() creates the file if it doesnt exist, then writes the string inside it.
If the file already exists it overwrites completely - old content is gone.
file_path = Path('data/notes.txt')

file_path.write_text('Hello World')

Critical warning:
file_path.write_text('First entry')
file_path.write_text('Second entry')  # 'First entry' is GONE!

print(file_path.read_text())  # 'Second entry'
To ADD to a file without deleting:
# write_text = overwrite (destructive)
file_path.write_text('replaces everything')

# open with 'a' = append (safe)
with open(file_path, 'a') as f:
    f.write('adds to the end\n')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 9: In plain English, what does each line do and why?
Plain English hint: Saving Python objects (lists, dicts) to disk so they survive after your program closes.
 import shelve

with shelve.open('mystorage') as shelf:
    shelf['contacts'] = [{'name': 'John'}, {'name': 'Jane'}]

//////////////////////////////////////////////////////////////////
Plain English:
shelve is like a persistent dictionary - saves Python objects directly to disk files.
with handles opening and closing automatically. Whatever you store in shelf['key'] survives after your program closes.

import shelve

with shelve.open('mystorage') as shelf:
    shelf['contacts'] = [{'name': 'John'}, {'name': 'Jane'}]
What makes shelve special vs write_text:
# write_text only saves strings
file_path.write_text("has to be a string")

# shelve saves ANY Python object directly
shelf['contacts'] = [{'name': 'John'}]  # List of dicts - no converting needed!
shelf['count'] = 42                      # Integer - works!
shelf['settings'] = {'theme': 'dark'}   # Dict - works!

The with block:
with shelve.open('mystorage') as shelf:
    # shelf is open and usable here
    shelf['key'] = value

# shelf is automatically closed and saved here

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 10: In plain English, what does each line do and why?
Plain English hint: Getting your saved data back out after closing and reopening.

import shelve

with shelve.open('mystorage') as shelf:
    contacts = shelf.get('contacts', [])
    print(contacts)

//////////////////////////////////////////////////////////////////
Plain English:
shelf.get('key', default) safely retrieves stored data.
If the key exists, returns the data. If not, returns the default value instead of crashing.
Essential for first-time program runs when no data exists yet.

import shelve

with shelve.open('mystorage') as shelf:
    contacts = shelf.get('contacts', [])
    print(contacts)
Why get() over direct access:
# Direct access - crashes if key missing
contacts = shelf['contacts']  # KeyError if first run!

# get() - safe, returns default instead
contacts = shelf.get('contacts', [])  # Returns [] if first run

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'os Module - File Info, Environment, Paths

Plain English Overview
os is an older module that talks to your operating system.
Youll see it everywhere in real Python code. pathlib (Path) is the modern replacement for most tasks,
but os is still used for things like environment variables, renaming, and deleting files.

os Module Summary
pythonimport os

os.getcwd()                          # Current directory (string)
os.chdir('folder')                   # Change directory
os.listdir('.')                      # List contents (list of strings)

os.path.exists('path')               # Exists?
os.path.isfile('path')               # Is file?
os.path.isdir('path')                # Is directory?

os.path.join('data', 'file.txt')     # Join paths safely
os.path.basename('data/file.txt')    # 'file.txt'
os.path.dirname('data/file.txt')     # 'data'
os.path.splitext('file.txt')         # ('file', '.txt')

os.rename('old.txt', 'new.txt')      # Rename/move
os.remove('file.txt')                # Delete file (permanent!)

os.getenv('KEY', 'default')          # Get environment variable
os.environ                           # All environment variables (dict)
os vs Path - quick reference:

os.getcwd()          →  Path.cwd()
os.path.exists()     →  path.exists()
os.path.isfile()     →  path.is_file()
os.path.join()       →  Path('/') / 'folder'
os.path.basename()   →  path.name
os.path.dirname()    →  path.parent
os.path.splitext()   →  path.stem / path.suffix
os.rename()          →  path.rename()
os.remove()          →  path.unlink()

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Concept 1: os.getcwd() and os.chdir()
Plain English:

getcwd() = "get current working directory" - tells you where Python is currently running from.
chdir() = "change directory" - moves Pythons working location to a different folder.

import os

print(os.getcwd())    # Shows current location
os.chdir('data')      # Move into 'data' folder
print(os.getcwd())    # Now shows new location


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Question 1: In plain English, what does each line do and why?
import os

current = os.getcwd()
print(f'Running from: {current}')

//////////////////////////////////////////////////////////////////
Plain English:
os.getcwd() returns the full path of where Python is currently running as a string.
Useful for knowing where files will be saved when you use relative paths.

import os

current = os.getcwd()
print(f'Running from: {current}')
# Running from: C:/Users/G/projects/python
Comparison with Path:
python# os version
current = os.getcwd()           # Returns string

# Path version (modern)
current = Path.cwd()            # Returns Path object
current = str(Path.cwd())       # Returns string

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 2: os.listdir()
Plain English:
Returns a list of everything (files and folders) inside a directory.
Like opening a folder in Windows Explorer and seeing the contents listed.

import os

contents = os.listdir('data')
print(contents)
# ['contacts.json', 'logs', 'backup.txt']

Question 2: In plain English, what does each line do and why?

import os

contents = os.listdir('.')
for item in contents:
    print(item)

//////////////////////////////////////////////////////////////////
Plain English:
'.' means "current directory" - a universal shorthand in programming.
os.listdir('.') lists everything in whatever folder Python is currently running from.

import os

contents = os.listdir('.')  # '.' = current directory
for item in contents:
    print(item)
# contacts.json
# logs
# backup.txt
# main.py

Common directory shortcuts:

os.listdir('.')   # Current directory
os.listdir('..')  # Parent directory (one level up)
os.listdir('data') # Specific folder

Comparison with Path:

# os version - returns list of strings
contents = os.listdir('data')

# Path version - returns Path objects
contents = list(Path('data').iterdir())

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 3: os.path.exists(), os.path.isfile(), os.path.isdir()

Plain English:
The os.path sub-module checks things about paths.
These three do exactly what Paths .exists(), .is_file(), .is_dir() do - just older syntax.

import os

os.path.exists('data/contacts.json')  # True or False
os.path.isfile('data/contacts.json')  # True or False
os.path.isdir('data')                 # True or False

    Question 3: In plain English, what does each line do and why?

import os

path = 'data/contacts.json'

if os.path.exists(path) and os.path.isfile(path):
    print('ready to read')

//////////////////////////////////////////////////////////////////
Plain English:
Two checks combined with and - confirms the path exists AND is specifically a file (not a folder) before proceeding.
Prevents crashes when trying to read something that doesnt exist or is the wrong type.

import os

path = 'data/contacts.json'

if os.path.exists(path) and os.path.isfile(path):
    print('ready to read')
os vs Path comparison:

# os version (older)
if os.path.exists(path) and os.path.isfile(path):
    pass

# Path version (modern)
p = Path(path)
if p.exists() and p.is_file():
    pass
Both do the same thing - youll see both in real code.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 4: os.path.join()
Plain English:
Combines folder and filename into one path safely. The old way of doing what Path / does now. Still common in older code.

import os

folder = 'data'
filename = 'contacts.json'

full_path = os.path.join(folder, filename)
print(full_path)  # 'data/contacts.json'

    Question 4: In plain English, what does each line do and why?

import os

base = 'C:/Users/G'
project = 'python'
filename = 'main.py'

full_path = os.path.join(base, project, filename)
print(full_path)

//////////////////////////////////////////////////////////////////
Plain English:
os.path.join() stitches any number of path pieces together with the correct separator automatically.
Works on any OS (Windows uses \, Mac/Linux use /).

import os

base = 'C:/Users/G'
project = 'python'
filename = 'main.py'

full_path = os.path.join(base, project, filename)
print(full_path)  # 'C:/Users/G/python/main.py'

Why it matters:

# Manual string - breaks on different OS
path = 'data' + '/' + 'contacts.json'  # Fails on Windows

# os.path.join - works everywhere
path = os.path.join('data', 'contacts.json')

# Path / operator - also works everywhere (modern)
path = Path('data') / 'contacts.json'


os vs Path comparison:

# os (older - you'll see this everywhere)
os.path.join('data', 'logs', 'error.txt')

# Path (modern - cleaner)
Path('data') / 'logs' / 'error.txt'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 5: os.path.basename() and os.path.dirname()
Plain English:
basename() = just the filename at the end. dirname() = just the folder part. The old way of what Path.name and Path.parent do now.

import os

path = 'data/logs/error.txt'

print(os.path.basename(path))  # 'error.txt'
print(os.path.dirname(path))   # 'data/logs'

    Question 5: In plain English, what does each line do and why?

import os

full_path = 'C:/Users/G/projects/main.py'

filename = os.path.basename(full_path)
folder = os.path.dirname(full_path)

print(f'File: {filename}')
print(f'Location: {folder}')

//////////////////////////////////////////////////////////////////
Plain English:
basename() extracts just the filename from the end of a full path as a string.
dirname() extracts just the folder portion as a string. Both return plain strings, not Path objects.

import os

full_path = 'C:/Users/G/projects/main.py'

filename = os.path.basename(full_path)  # 'main.py'     (string)
folder = os.path.dirname(full_path)     # 'C:/Users/G/projects' (string)

print(f'File: {filename}')      # File: main.py
print(f'Location: {folder}')   # Location: C:/Users/G/projects
os vs Path comparison:

path = 'C:/Users/G/projects/main.py'

# os version (returns strings)
os.path.basename(path)   # 'main.py'
os.path.dirname(path)    # 'C:/Users/G/projects'

# Path version (returns Path objects)
Path(path).name          # 'main.py'
Path(path).parent        # Path('C:/Users/G/projects')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 6: os.path.splitext()
Plain English:
Splits a filename into two parts - the name and the extension. Useful when you need to check or change file types.

import os

filename = 'contacts.json'
name, ext = os.path.splitext(filename)
print(name)  # 'contacts'
print(ext)   # '.json'

    Question 6: In plain English, what does each line do and why?
pythonimport os

files = ['data.json', 'notes.txt', 'image.png']

for file in files:
    name, ext = os.path.splitext(file)
    print(f'{name} is a {ext} file')

//////////////////////////////////////////////////////////////////
Plain English:
splitext() just splits at the LAST dot in the string - it doesn't know or validate file types. It's purely mechanical string splitting.

import os

# Normal case
name, ext = os.path.splitext('contacts.json')
# name = 'contacts'   ext = '.json'

# Multiple dots - splits at LAST dot
name, ext = os.path.splitext('my.backup.contacts.json')
# name = 'my.backup.contacts'   ext = '.json'

# No extension
name, ext = os.path.splitext('README')
# name = 'README'   ext = ''

# Random dot
name, ext = os.path.splitext('my.randomword')
# name = 'my'   ext = '.randomword'  (no error!)

# Dot at start (hidden files on Linux)
name, ext = os.path.splitext('.hidden')
# name = '.hidden'   ext = ''  (treats as no extension)

Your regex analogy is spot on - its just grouping around the last dot, no validation.
os vs Path comparison:

# os version
name, ext = os.path.splitext('contacts.json')

# Path version
p = Path('contacts.json')
name = p.stem      # 'contacts'
ext  = p.suffix    # '.json'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 7: os.rename() and os.remove()
Plain English:
rename() renames OR moves a file. remove() permanently deletes a file. No recycle bin - its gone!

import os

os.rename('old_name.txt', 'new_name.txt')  # Rename
os.remove('unwanted.txt')                   # Delete permanently

    Question 7: In plain English, what does each line do and why?

import os

old = 'data/contacts.json'
new = 'data/contacts_backup.json'

if os.path.exists(old):
    os.rename(old, new)
    print('renamed!')

//////////////////////////////////////////////////////////////////
Plain English:
Always check exists() before renaming or deleting - attempting these on missing files crashes your program. The if guard makes it safe.

import os

old = 'data/contacts.json'
new = 'data/contacts_backup.json'

if os.path.exists(old):
    os.rename(old, new)
    print('renamed!')
os.remove() warning:

# PERMANENT - no recycle bin!
os.remove('important.txt')  # Gone forever

# Safe version always check first
if os.path.exists('important.txt'):
    os.remove('important.txt')
os vs Path comparison:

# os version
os.rename('old.txt', 'new.txt')
os.remove('file.txt')

# Path version (modern)
Path('old.txt').rename('new.txt')
Path('file.txt').unlink()  # Path's delete method


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 8: os.environ and os.getenv()

Plain English:
Environment variables are settings stored by your operating system -
things like your username, system paths, or secret keys.
os.environ is a dictionary of all of them. os.getenv() safely gets one by name.

import os

# All environment variables (big dictionary)
print(os.environ)

# Get one specific variable
username = os.getenv('USERNAME')
print(username)  # 'G'

    Question 8: In plain English, what does each line do and why?

import os

api_key = os.getenv('MY_API_KEY', 'not set')
print(f'API Key: {api_key}')

//////////////////////////////////////////////////////////////////
Plain English:
os.getenv('KEY', default) safely gets an environment variable.
The second argument is the fallback value if the key doesnt exist - same idea as shelf.get('key', default) from earlier.

import os

api_key = os.getenv('MY_API_KEY', 'not set')
print(f'API Key: {api_key}')
# API Key: not set  (if not defined)
# API Key: abc123   (if defined)

Why environment variables matter:

# BAD - hardcoded secret in your code
api_key = 'abc123secretkey'  # Anyone who sees your code gets your key!

# GOOD - stored in OS environment, not in code
api_key = os.getenv('MY_API_KEY')  # Key stays hidden
Common use:

import os

# Check before using
db_password = os.getenv('DB_PASSWORD')

if db_password is None:
    print('Error: DB_PASSWORD not set in environment')
else:
    print('Connecting to database...')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
'glob / Path.glob() - Finding Files by Pattern

Plain English Overview:
glob finds files matching a pattern -
like a search with wildcards. Instead of listing ALL files and filtering manually,
you describe what youre looking for and glob returns only matching files.

The two ways:

import glob                    # Old way
from pathlib import Path       # Modern way (Path.glob)

//////////////////////////////////////////////////////////////////
glob Summary

import glob
from pathlib import Path

# glob module (old - returns strings)
glob.glob('*.txt')              # All .txt in current dir
glob.glob('data/*.json')        # All .json in data/
glob.glob('**/*.py')            # All .py recursively

# Path.glob (modern - returns Path objects)
Path('data').glob('*.txt')      # All .txt in data/
Path('data').glob('**/*.json')  # All .json recursively

# Common patterns
'*.txt'         # Any .txt file
'data_*'        # Starts with data_
'report_*.pdf'  # report_ then anything then .pdf
'**/*.py'       # All .py files in all subfolders

# With filtering
files = [f for f in Path('data').glob('*.json') if f.is_file()]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 1: The * Wildcard

Plain English:
* means "match anything" - zero or more characters. Like a blank tile in Scrabble.

*.txt           # Any file ending in .txt
data_*          # Any file starting with data_
*.json          # Any file ending in .json

    Question 1: In plain English, what would these patterns find?

'*.txt'
'report_*.pdf'
'*.py'

//////////////////////////////////////////////////////////////////
Plain English:

* fills in for any characters in that position. Think of it as a wildcard placeholder that matches anything.

'*.txt'        # notes.txt, data.txt, anything.txt
'report_*.pdf' # report_2024.pdf, report_jan.pdf
'*.py'         # main.py, helper.py, test.py

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 2: Basic glob.glob()
Plain English:
glob.glob(pattern) searches for files matching your pattern and returns a list of matching file paths as strings.

import glob

results = glob.glob('*.txt')
print(results)
# ['notes.txt', 'readme.txt', 'data.txt']

    Question 2: In plain English, what does each line do and why?

import glob

txt_files = glob.glob('data/*.txt')
for file in txt_files:
    print(file)

//////////////////////////////////////////////////////////////////
Plain English:

glob.glob('data/*.txt') searches inside the data folder specifically for .txt files.
It searches relative to wherever Python is currently running (os.getcwd()).

import glob

txt_files = glob.glob('data/*.txt')
for file in txt_files:
    print(file)
# data/notes.txt
# data/readme.txt
# data/contacts.txt
Returns empty list if nothing found:

results = glob.glob('data/*.xyz')
print(results)  # []  (no error, just empty)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 3: Path.glob() - The Modern Way

Plain English:
Path.glob() does the same thing but returns Path objects instead of strings - giving you all the Path tools on each result.
from pathlib import Path

data_dir = Path('data')
results = data_dir.glob('*.txt')

for file in results:
    print(file)

    Question 3: In plain English, what does each line do and why?

from pathlib import Path

data_dir = Path('data')

for file in data_dir.glob('*.json'):
    print(file.name)
    print(file.stem)

//////////////////////////////////////////////////////////////////
Plain English:
Each result from glob() is a full Path object,
giving you access to all Path attributes like .name and .stem immediately on each found file.

from pathlib import Path

data_dir = Path('data')

for file in data_dir.glob('*.json'):
    print(file.name)   # 'contacts.json'  (full filename WITH extension)
    print(file.stem)   # 'contacts'        (filename WITHOUT extension)

Memory trick again:

.name = full name (contacts.json)
.stem = stem/base only (contacts)

glob vs Path.glob comparison:

# glob (returns strings)
import glob
results = glob.glob('data/*.json')
for f in results:
    print(f)           # 'data/contacts.json' (string)

# Path.glob (returns Path objects)
from pathlib import Path
results = Path('data').glob('*.json')
for f in results:
    print(f.name)      # 'contacts.json' (Path tools available!)
    print(f.stem)      # 'contacts'
    print(f.suffix)    # '.json'
    print(f.parent)    # Path('data')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 4: The ** Wildcard (Recursive)
Plain English:
** means "search through ALL subfolders too." Single * only looks in one folder. Double ** digs through everything underneath.

# * = one folder only
data_dir.glob('*.txt')          # Only in 'data/'

# ** = all subfolders too
data_dir.glob('**/*.txt')       # data/ AND data/logs/ AND data/backup/ etc.

    Question 4: In plain English, what does each line do and why?

from pathlib import Path

project = Path('myproject')

for file in project.glob('**/*.py'):
    print(file)

//////////////////////////////////////////////////////////////////
Plain English:
**/*.py digs through every subfolder inside myproject at any depth and returns all .py files found anywhere inside.

from pathlib import Path

project = Path('myproject')

for file in project.glob('**/*.py'):
    print(file)
# myproject/main.py
# myproject/utils/helper.py
# myproject/utils/tools/parser.py
# myproject/tests/test_main.py

Depth comparison:

# One level only
project.glob('*.py')        # myproject/main.py  only

# One level down
project.glob('*/*.py')      # myproject/utils/helper.py  only

# All levels (recursive)
project.glob('**/*.py')     # Everything everywhere

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
    Concept 5: Filtering Results
Plain English:
Combine glob with conditions to filter results further - like finding only large files or recently modified ones.

from pathlib import Path

data_dir = Path('data')

for file in data_dir.glob('*.txt'):
    if file.is_file():
        print(file.name)


    Question 5: In plain English, what does each line do and why?

from pathlib import Path

data_dir = Path('data')
json_files = [f for f in data_dir.glob('*.json') if f.is_file()]
print(f'Found {len(json_files)} json files')

//////////////////////////////////////////////////////////////////
Plain English:

List comprehension with glob filters results in one clean line.
The is_file() check excludes anything that matches the pattern but isnt actually a file (like a folder named data.json).
from pathlib import Path

data_dir = Path('data')
json_files = [f for f in data_dir.glob('*.json') if f.is_file()]
print(f'Found {len(json_files)} json files')
# Found 3 json files

Without list comprehension (same thing, more lines):

json_files = []
for f in data_dir.glob('*.json'):
    if f.is_file():
        json_files.append(f)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

open
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









