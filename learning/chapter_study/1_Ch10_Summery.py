Ch 10 Reading and Writing Files

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Path() — Building Cross-Platform File Paths

What it is:
    Path() from the pathlib module constructs a file path that works correctly on any operating system,
    handling the backslash vs. forward slash difference automatically.
    You pass each folder name as a separate argument, or join path segments using the / operator on a Path object.

Why it matters:
    Hardcoding \ backslashes for Windows breaks your code on Mac/Linux — Path() removes that problem entirely.

Example:
from pathlib import Path

Path('Users', 'Al', 'Documents')        # builds the correct path for your OS
Path('Users') / 'Al' / 'Documents'      # same result using / operator

Path('C:/Users') / 'Al'  # works — Path object
'C:/Users' / 'Al'        # TypeError — plain string

# Appending filenames to a base path
for filename in ['a.txt', 'b.csv']:
    print(Path(r'C:\Users\Al') / filename)

Gotcha:
    The / operator requires at least the leftmost value to be a Path object — using / between two plain strings raises a TypeError.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Path.cwd() and os.chdir() — Working Directory

What it is:
    The current working directory is the folder your program treats as its "home base" for relative paths.
    Path.cwd() returns it as a Path object; os.chdir() changes it.

Why it matters:
    Any filename without a full path is resolved relative to the working directory —
    knowing and controlling it prevents silent file-not-found errors.

Methods at a glance:

Path.cwd() — returns the current working directory as a Path object
os.chdir() — changes the current working directory to the path you pass in

Example:
from pathlib import Path
import os

Path.cwd()                    # WindowsPath('C:/Users/Al/...')
os.chdir('C:/Windows')
Path.cwd()                    # WindowsPath('C:/Windows')

Gotcha:
    There is no pathlib equivalent for changing the working directory — you must use os.chdir() for that.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Path.home() — Home Directory

What it is:
    Path.home() returns a Path object pointing to the current users home folder —
    the standard personal directory that exists on every OS.

Why it matters:
    Your scripts are almost always guaranteed read/write access there, making it the safest default location for saving files.

Example:
Path.home()    # WindowsPath('C:/Users/Al')

# Safe place to save a file
save_path = Path.home() / 'my_output.txt'

Gotcha:
    Home directory locations differ by OS — C:\Users\name on Windows, /Users/name on macOS, /home/name on Linux.
    Always use Path.home() rather than hardcoding any of these.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Absolute vs. Relative Paths

What it is:
    An absolute path starts from the root folder and gives the full location of a file regardless of where your program is running.
    A relative path is shorter and describes a location starting from the current working directory.
    The special names . (current folder) and .. (parent folder) can be used inside relative paths.

Why it matters:
    Understanding the difference prevents files being created or read from unexpected locations when your working directory changes.

Methods at a glance:

.is_absolute() — returns True if the path starts from root, False if relative
.absolute() — converts a relative path to absolute using the current working directory

Example:
Path('spam/eggs').is_absolute()           # False
Path('C:/Users/Al').is_absolute()         # True

Path('spam/eggs').absolute()              # full path from cwd
Path.cwd() / Path('spam/eggs')            # same result manually
Path.home() / Path('spam/eggs')           # absolute from home instead

Gotcha:
    ./ at the start of a relative path is optional — spam.txt and ./spam.txt refer to the same file.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Creating Folders — os.makedirs() and Path.mkdir()

What it is:
    os.makedirs() creates a folder and any missing parent folders in one call.
    Path.mkdir() does the same from a Path object, but only creates the final folder unless you pass parents=True.

Why it matters:
    Trying to write a file to a folder that doesnt exist raises an error — creating the path first prevents that.

Methods at a glance:

os.makedirs() — creates the full folder chain in one shot, no matter how deep
Path.mkdir() — creates a single folder from a Path object; add parents=True to create the full chain

Example:
import os
os.makedirs('C:/delicious/walnut/waffles')   # creates all three folders

from pathlib import Path
Path(r'C:\Users\Al\newFolder').mkdir()                  # one folder only
Path(r'C:\Users\Al\a\b\c').mkdir(parents=True)          # full chain

Gotcha:
    Path.mkdir() fails with an error if parent folders don't exist and you haven't passed parents=True.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Path Attributes — Extracting Parts of a Filepath

What it is:
    Path objects expose their components as named attributes —
    you can pull out just the filename, extension, parent folder, or root without doing any string splitting yourself.

Why it matters:
    Lets you build new paths from parts of existing ones, like renaming a file while keeping its folder and extension.

Attributes at a glance:

.name — full filename including extension (spam.txt)
.stem — filename without extension (spam)
.suffix — extension only (.txt)
.parent — the containing folder as a Path object
.anchor — root folder (C:\ or /)
.parts — tuple of every component in the path
.parents[n] — ancestor folders by index (0 = immediate parent)

Example:
p = Path('C:/Users/Al/spam.txt')

p.name      # 'spam.txt'
p.stem      # 'spam'
p.suffix    # '.txt'
p.parent    # WindowsPath('C:/Users/Al')
p.anchor    # 'C:\\'
p.parts     # ('C:\\', 'Users', 'Al', 'spam.txt')

Path.cwd().parents[0]   # immediate parent of cwd
Path.cwd().parents[1]   # grandparent of cwd

Gotcha:
    .parent (singular) returns a single Path object for the immediate parent;
    .parents (plural) is an indexed sequence of all ancestors — they are two different things.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    .stat() — File Size and Timestamps

What it is:
    Calling .stat() on a Path object returns a result object containing metadata about the file —
    its size in bytes and several timestamps.
    The timestamps are in Unix epoch time (seconds since Jan 1, 1970) and need the time module to convert to a readable format.

Why it matters:
    Useful for checking file sizes, finding when a file was last changed, or sorting files by date.

Example:
from pathlib import Path
import time

f = Path('C:/Windows/System32/calc.exe')
f.stat().st_size                                      # size in bytes
f.stat().st_size / 1024                               # size in KB

time.asctime(time.localtime(f.stat().st_mtime))       # human-readable modified date
Key attributes: st_size (bytes), st_mtime (last modified), st_ctime (created/metadata changed), st_atime (last accessed)

Gotcha:
    Timestamps can be changed manually and are not guaranteed accurate —
    dont rely on them for security-sensitive checks.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    .glob() — Finding Files by Pattern

What it is:
    Calling .glob() on a folder Path object returns all files and subfolders matching a glob pattern —
    * matches any text, ? matches exactly one character. It returns a generator, so pass it to list() or use it directly in a for loop.

Why it matters:
    Lets you find all files of a specific type (e.g. all .txt files) in a folder without listing everything manually.

Example:
from pathlib import Path

p = Path('C:/Users/Al/Desktop')

list(p.glob('*.txt'))           # all .txt files
list(p.glob('project?.txt'))    # project1.txt, project2.txt, etc.
list(p.glob('*'))               # everything in the folder

for f in p.glob('*.csv'):
    print(f)
Gotcha:
    glob() returns a generator object, not a list —
    calling len() on it directly or indexing it wont work without wrapping it in list() first.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Path Validity — exists(), is_file(), is_dir()

What it is:
    These three Path methods let you check whether a path actually exists on disk
    and whether it points to a file or a folder, each returning True or False.

Why it matters:
    Prevents crashes when your code tries to open or write to a path that doesnt exist yet.

Methods at a glance:

.exists() — True if the path exists at all, file or folder
.is_file() — True if the path exists and is a file
.is_dir() — True if the path exists and is a directory

Example:
p = Path('C:/Windows')
p.exists()     # True
p.is_dir()     # True
p.is_file()    # False

Path('C:/fake/path').exists()    # False — no crash, just False

Gotcha:
    A path can pass .exists() but still fail .is_file() — always use the specific check that matches what your code actually needs.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Reading and Writing Files — open(), read(), readlines(), write(), close()

What it is:
    open() connects your program to a file on disk and returns a file object.
    You then call methods on that object to read or write content, and call close() when done.
    The mode you pass determines whether you can read ('r'), overwrite ('w'), or append ('a').

Why it matters:
    This is the standard way to get data into and out of files in Python — variables vanish when the program ends, files persist.

Methods at a glance:

open(path, mode, encoding) — opens a file, returns a file object; default mode is 'r'
.read() — returns the entire file contents as a single string
.readlines() — returns a list of strings, one per line (each includes \n)
readline()   # returns just the first line (that's the one-line version)
.write(string) — writes a string to the file, returns character count
.close() — saves and releases the file; required before reopening

Example:
# Write
f = open('notes.txt', 'w', encoding='utf-8')
f.write('First line\n')
f.close()

# Append
f = open('notes.txt', 'a', encoding='utf-8')
f.write('Second line\n')
f.close()

# Read
f = open('notes.txt', encoding='utf-8')
print(f.read())
f.close()

Gotcha:
    write() does not add a newline automatically — you must include \n yourself, unlike print().

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    with Statements — Automatic File Closing

What it is:
    A with statement opens a file, runs your code block, and automatically calls close() when the block ends —
    even if an error occurs mid-block. The file object is assigned using as.

Why it matters:
    Forgetting close() can cause data loss or lock files — with makes it impossible to forget.

Example:
# Without with — easy to forget close()
f = open('data.txt', 'w', encoding='utf-8')
f.write('Hello')
f.close()

# With with — close() is automatic
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello')

with open('data.txt', encoding='utf-8') as f:
    content = f.read()

Gotcha:
    Variables assigned inside a with block (like content above) are still accessible after the block ends —
    only the file object is closed, not the data you read from it.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    shelve — Saving Python Variables to Disk

What it is:
    The shelve module lets you save Python variables directly to a binary file and reload them later,
    using a dictionary-like interface. You open a shelf with shelve.open(), store values by key, and call .close() when done.

Why it matters:
    Lets your program remember data between runs —
    like a simple Save feature — without you having to manually convert data to and from text.

Methods at a glance:

shelve.open(filename) — opens or creates a shelf file, returns a shelf object
shelf['key'] = value — stores any Python value under a key
shelf['key'] — retrieves the value for that key
.keys() / .values() — work like dictionary methods; wrap in list() to view
.close() — saves and closes the shelf

Example:
import shelve

# Save
shelf = shelve.open('mydata')
shelf['cats'] = ['Zophie', 'Pooka', 'Simon']
shelf.close()

# Load
shelf = shelve.open('mydata')
print(shelf['cats'])     # ['Zophie', 'Pooka', 'Simon']
shelf.close()

Gotcha:
    shelve creates multiple files on Windows (.bak, .dat, .dir) and a single file on macOS/Linux —
    dont delete or rename any of them individually or the shelf will break.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Summary:

Path() builds cross-platform paths; use / to join segments — the leftmost value must be a Path object

Path.cwd() gets the working directory; os.chdir() changes it; Path.home() points to the users home folder

Path attributes (.name, .stem, .suffix, .parent, .parts) extract components without string parsing

.glob() finds files by pattern; .exists(), .is_file(), .is_dir() check validity before acting

open() with modes 'r'/'w'/'a' handles reading, overwriting, and appending — always use encoding='utf-8'

Use with open(...) as f: instead of manual open()/close() pairs — automatic and safer

shelve saves Python objects directly to disk with a dictionary interface — the right tool when persisting structured data between runs

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
