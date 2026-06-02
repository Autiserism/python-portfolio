
'Chapter 10 File Operations - Syntax Drilling

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Session 1: Path Basics (pathlib)
The Path object is your main tool for file operations.

    Round 1 - Creating Path Objects
from pathlib import Path

# Three ways to create paths
Question: Complete these three patterns:

Current directory: Path(___)
Specific path: Path(___)
Home directory: Path.___

Path.cwd() - current working directory
Path() - needs a string inside
Path.home() - home directory

/////////////////////////////////////////////////////////////

Correct patterns:
from pathlib import Path

# 1. Current directory
current = Path.cwd()
print(current)  # /home/user/projects

# 2. Specific path (string inside)
file_path = Path('data/contacts.json')
folder = Path('logs')

# 3. Home directory
home = Path.home()
print(home)  # /home/user
Key point: Path() needs a string: Path('filename.txt')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - Building Paths with /
The / operator joins paths (cleaner than string concatenation).
Question: Complete this pattern:
folder = Path('data')
filename = 'contacts.json'

# Join them
full_path = folder ___ filename

folder = Path('data')
filename = 'contacts.json'

full_path = folder / filename
print(full_path)  # data/contacts.json

/////////////////////////////////////////////////////////////

The / operator is magical for paths!

# Build complex paths
base = Path.home()
project = base / 'projects' / 'python' / 'W3P5'
data_file = project / 'data' / 'contacts.json'

print(data_file) # /home/user/projects/python/W3P5/data/contacts.json

Why / is better than strings:

# Bad (manual string joining)
path = 'data' + '/' + 'contacts.json'  # Breaks on Windows

# Good (automatic OS handling)
path = Path('data') / 'contacts.json'  # Works everywhere

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Common Path Attributes
Question: What do these return?
p = Path('/home/user/projects/data/contacts.json')

p.name      # ???
p.stem      # ???
p.suffix    # ???
p.parent    # ???

/////////////////////////////////////////////////////////////

p = Path('/home/user/projects/data/contacts.json')

p.name      # 'contacts.json'  (full filename)
p.stem      # 'contacts'        (without extension)
p.suffix    # '.json'           ✓ Correct!
p.parent    # Path('.../data')  ✓ Correct!
Memory trick:

name = full filename (with extension)
stem = stem of flower (base without the bloom/extension)

More examples:
p = Path('reports/sales_2024.xlsx')

print(p.name)    # 'sales_2024.xlsx'
print(p.stem)    # 'sales_2024'
print(p.suffix)  # '.xlsx'
print(p.parent)  # Path('reports')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 4 - Checking Path Types
Question: Complete these checks:
p = Path('data/contacts.json')

# Check if exists
p.___()

# Check if file
p.___()

# Check if directory
p.___()

/////////////////////////////////////////////////////////////

p = Path('data/contacts.json')

p.exists()    # True if exists (file or directory)
p.is_file()   # True if it's a file
p.is_dir()    # True if it's a directory

All three need ():
if p.exists():
    print("Path exists!")

    if p.is_file():
        print("It's a file")
    elif p.is_dir():
        print("It's a directory")
Common pattern:
# Safe file reading
p = Path('contacts.json')

if p.exists() and p.is_file():
    content = p.read_text()
else:
    print("File not found!")


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - Reading Files
Three methods for reading:
Question: Complete these patterns:

p = Path('data.txt')

# Read entire file as string
content = p.___()

# Read as list of lines
lines = p.___()

# Read binary data
data = p.___()

/////////////////////////////////////////////////////////////

p = Path('data.txt')

# Read entire file as string
content = p.read_text()  # Not read()

# Read as list of lines (need to split)
lines = p.read_text().splitlines()  # No readline() method

# Read binary data
data = p.read_bytes()  # Not readbin()
The three Path read methods:

read_text() - returns string
read_bytes() - returns bytes
No readlines() - must split manually or use open()

Examples:
# String content
p = Path('notes.txt')
content = p.read_text()
print(content)  # "Line 1\nLine 2\nLine 3"

# List of lines
lines = p.read_text().splitlines()
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Binary data (images, etc.)
img = Path('photo.jpg')
data = img.read_bytes()
Pattern to memorize:

read_text() → string
read_bytes() → bytes
.splitlines() → list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - Writing Files
Question: Complete these patterns:
p = Path('output.txt')

# Write string to file
p.___(content)

# Write bytes to file
p.___(data)

# Append to file (not overwrite)
# Hint: No direct method, use open()

/////////////////////////////////////////////////////////////

p = Path('output.txt')

# 1. Write string to file
p.write_text('Hello world')  # Overwrites file

# 2. Write bytes to file
p.write_bytes(b'Binary data')  # Overwrites file

# 3. Append to file (no Path method)
# Your approach is correct!
with open(p, 'a', encoding='utf-8') as f:
    f.write('appended text\n')
Pattern:

write_text(string) → overwrites with string
write_bytes(data) → overwrites with bytes
For append → use open(p, 'a')

Important: write_text() and write_bytes() always overwrite!
# This overwrites each time!
p.write_text('First')
p.write_text('Second')  # "First" is gone!

print(p.read_text())  # "Second"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 7 - Creating Directories
Question: Complete these patterns:
# Create single directory
Path('logs').___()

# Create directory + all parents (like mkdir -p)
Path('data/json/backups').___()

# Check if directory exists before creating
p = Path('logs')
if not p.___():
    p.___()

/////////////////////////////////////////////////////////////

# 1. Create single directory
Path('logs').mkdir()  # ✓ Correct

# 2. Create directory + all parents
Path('data/json/backups').mkdir(parents=True)  # Not makedirs()

# 3. Check if exists before creating
p = Path('logs')
if not p.exists():
    p.mkdir()  # Not cwd()!
The mkdir() parameters:
# Basic (fails if parent doesn't exist)
Path('logs').mkdir()

# Create parents too
Path('data/logs/2024').mkdir(parents=True)

# Don't error if exists
Path('logs').mkdir(exist_ok=True)

# Both together (most common)
Path('data/logs/2024').mkdir(parents=True, exist_ok=True)
Pattern to memorize:
# Safe directory creation (never fails)
output_dir = Path('data/processed/2024')
output_dir.mkdir(parents=True, exist_ok=True)

Common mistake:
# This FAILS if 'data' doesn't exist
Path('data/logs').mkdir()  # FileNotFoundError!

# This works
Path('data/logs').mkdir(parents=True)  # Creates 'data' then 'logs'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

'Session 2: shelve Module
shelve saves Python objects to disk (like a persistent dictionary).

    Round 8 - Basic shelve Operations
Question: Complete this pattern:
import shelve

# Open shelf file
shelf = shelve.___(___)

# Save data
shelf['key'] = value

# Read data
value = shelf['key']

# Close shelf
shelf.___()

/////////////////////////////////////////////////////////////

import shelve

# Open shelf file (give it a filename)
shelf = shelve.open('mydata')  # Not 'key'

# Save data (key is the dictionary key)
shelf['contacts'] = contact_list
shelf['settings'] = {'theme': 'dark'}

# Read data
contacts = shelf['contacts']

# Close shelf
shelf.close()
Better - use with (auto-closes):
import shelve

# Automatically closes when done
with shelve.open('mydata') as shelf:
    shelf['contacts'] = contact_list
    shelf['score'] = 42
Key points:

shelve.open('filename') - filename without extension
Creates files: mydata.db, mydata.dat, etc.
Works like a dictionary: shelf['key'] = value
Always close or use with

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 9 - shelve with Path
Question: Combine Path and shelve:
from pathlib import Path
import shelve

# Create data directory
data_dir = Path('data')
data_dir.___(___)

# Open shelf in that directory
shelf_path = data_dir / 'contacts'
with shelve.open(___) as shelf:
    shelf['name'] = 'John'

/////////////////////////////////////////////////////////////

from pathlib import Path
import shelve

# Create data directory
data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)  # Add exist_ok

# Open shelf in that directory
shelf_path = data_dir / 'contacts'
with shelve.open(str(shelf_path)) as shelf:  # Convert Path to string
    shelf['name'] = 'John'
Key point: shelve.open() needs a string, not Path object.
# Wrong
with shelve.open(shelf_path):  # Path object fails

# Right
with shelve.open(str(shelf_path)):  # Convert to string
Complete working example:
from pathlib import Path
import shelve

# Setup
data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

contacts = [
    {'name': 'John', 'phone': '555-1234'},
    {'name': 'Jane', 'phone': '555-5678'}
]

# Save
shelf_file = data_dir / 'contacts'
with shelve.open(str(shelf_file)) as shelf:
    shelf['all_contacts'] = contacts
    shelf['count'] = len(contacts)

# Load
with shelve.open(str(shelf_file)) as shelf:
    loaded = shelf['all_contacts']
    print(loaded)  # [{'name': 'John', ...}, ...]


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 10 - shelve Keys and Values
Question: Complete these operations:
with shelve.open('data') as shelf:
    # Get all keys
    keys = list(shelf.___)

    # Check if key exists
    if 'contacts' ___ shelf:
        data = shelf['contacts']

    # Get with default (like dict)
    value = shelf.___(key, default)

with shelve.open('data') as shelf:
    # Get all keys
    keys = list(shelf.keys())  # ✓

    # Check if key exists
    if 'contacts' in shelf:  # ✓
        data = shelf['contacts']

    # Get with default (like dict)
    value = shelf.get(key, default)  # Not setdefault!
Difference:
# get() - just returns, doesn't modify
value = shelf.get('missing', [])  # Returns [], shelf unchanged

# setdefault() - sets AND returns
value = shelf.setdefault('missing', [])  # Sets shelf['missing'] = []

/////////////////////////////////////////////////////////////

Common shelf operations:
with shelve.open('data') as shelf:
    # Check what's stored
    print(list(shelf.keys()))

    # Safe access
    contacts = shelf.get('contacts', [])

    # Check existence
    if 'settings' in shelf:
        settings = shelf['settings']

    # Iterate
    for key in shelf:
        print(f"{key}: {shelf[key]}")

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

'Session 3: Workflow Practice
Lets combine Path, shelve, and file operations into realistic workflows.

Workflow 1 - Save Contact List
Scenario: Save W3P5 contacts to disk in multiple formats.
Question: Complete this workflow:

from pathlib import Path
import shelve
import json

contacts = [
    {'name': 'John', 'phone': '555-1234'},
    {'name': 'Jane', 'phone': '555-5678'}
]

# 1. Create data directory
data_dir = Path('___')
data_dir.___(___, ___)

# 2. Save as JSON
json_file = data_dir / '___'
json_file.___(json.dumps(contacts, indent=2))

# 3. Save with shelve
shelf_file = data_dir / '___'
with shelve.open(___) as shelf:
    shelf['___'] = contacts

/////////////////////////////////////////////////////////////

from pathlib import Path
import shelve
import json

contacts = [
    {'name': 'John', 'phone': '555-1234'},
    {'name': 'Jane', 'phone': '555-5678'}
]

# 1. Create data directory ✓
data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

# 2. Save as JSON
json_file = data_dir / 'contacts.json'  # Add .json extension
json_file.write_text(json.dumps(contacts, indent=2))  # write_text not open

# 3. Save with shelve
shelf_file = data_dir / 'contacts_shelf'  # Different name from json
with shelve.open(str(shelf_file)) as shelf:  # str() conversion
    shelf['contacts'] = contacts  # Descriptive key
Key corrections:

JSON files need .json extension
Use write_text() not open()
shelve.open() needs str(Path)
Use descriptive shelf keys

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Workflow 2 - Load Contact List
Question: Load from both formats:

from pathlib import Path
import shelve
import json

data_dir = Path('data')

# 1. Load from JSON
json_file = data_dir / 'contacts.json'
if json_file.___() and json_file.___():
    content = json_file.___()
    contacts = json.___(content)

# 2. Load from shelve
shelf_file = data_dir / 'contacts_shelf'
with shelve.open(___) as shelf:
    contacts = shelf.___('contacts', ___)
/////////////////////////////////////////////////////////////
from pathlib import Path
import shelve
import json

data_dir = Path('data')

# 1. Load from JSON
json_file = data_dir / 'contacts.json'
if json_file.exists() and json_file.is_file():  # exists() not exist()
    content = json_file.read_text()  # READ not write!
    contacts = json.loads(content)   # loads() not read_text()

# 2. Load from shelve
shelf_file = data_dir / 'contacts_shelf'
with shelve.open(str(shelf_file)) as shelf:  # shelf_file not json_file!
    contacts = shelf.get('contacts', [])  # [] not "default"
Key corrections:

exists() not exist() (with 's')
read_text() for reading, write_text() for writing
json.loads(string) - "load string"
Use correct variable (shelf_file not json_file)
Default should be actual value like []

Memory tricks:

read_text() ← reads
write_text() ← writes
json.dumps() ← dump to string
json.loads() ← load from string

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Workflow 3 - Safe File Operations

Question: Write a function that safely saves data with backup:
from pathlib import Path
import json

def safe_save(data, filename):
    """Save data to JSON with backup"""
    file_path = Path(filename)

    # 1. If file exists, create backup
    if file_path.___():
        backup = file_path.___ / (file_path.___ + '.backup')
        backup.___(___)

    # 2. Save new data
    file_path.___(json.dumps(data, indent=2))

/////////////////////////////////////////////////////////////

from pathlib import Path
import json
def safe_save(data, filename):
    """Save data to JSON with backup"""
    file_path = Path(filename)

    # 1. If file exists, create backup
    if file_path.exists():
        # parent = directory, name = filename
        backup = file_path.parent / (file_path.name + '.backup')
        # Copy content, not make directory!
        backup.write_text(file_path.read_text())

    # 2. Save new data ✓
    file_path.write_text(json.dumps(data, indent=2))
Key corrections:

file_path.parent - parent directory
file_path.name - filename (not .data)
backup.write_text() - copy the file content
Not mkdir() - thats for directories!

Attributes to remember:

p = Path('data/contacts.json')

p.parent  # Path('data')
p.name    # 'contacts.json'
p.stem    # 'contacts'
p.suffix  # '.json'

Better backup pattern:

from pathlib import Path
import json
import shutil

def safe_save(data, filename):
    file_path = Path(filename)

    # Create parent directory if needed
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Backup if exists
    if file_path.exists():
        backup = file_path.with_suffix('.json.backup')
        shutil.copy(file_path, backup)

    # Save
    file_path.write_text(json.dumps(data, indent=2))

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Workflow 4 - Complete Save/Load System

Question: Build a complete data manager:
from pathlib import Path
import shelve
import json

class DataManager:
    def __init__(self, data_dir='data'):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(___, ___)

    def save_json(self, data, filename):
        file_path = self.data_dir / filename
        file_path.___(json.dumps(data, indent=2))

    def load_json(self, filename):
        file_path = self.data_dir / filename
        if file_path.___():
            return json.___(file_path.___())
        return None

    def save_shelf(self, key, data):
        shelf_file = self.data_dir / 'storage'
        with shelve.open(___) as shelf:
            shelf[___] = ___

    def load_shelf(self, key):
        shelf_file = self.data_dir / 'storage'
        with shelve.open(___) as shelf:
            return shelf.___(key, None)

# Use it
dm = DataManager()
dm.save_json({'name': 'John'}, 'contact.json')
data = dm.load_json('contact.json')

/////////////////////////////////////////////////////////////



------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


/////////////////////////////////////////////////////////////


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------



/////////////////////////////////////////////////////////////

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
