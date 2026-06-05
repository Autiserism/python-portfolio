Chapter 11 Summary
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
shutil — Copying Files and Folders
What it is: The shutil module provides functions for copying files and entire folder trees. shutil.copy() copies a single file; shutil.copytree() copies a whole folder and everything inside it to a new location.
Why it matters: Lets your program duplicate files or create full folder backups in one call instead of manually recreating the structure.
Functions at a glance:

shutil.copy(src, dst) — copies a single file; if dst is a folder, keeps original filename; if dst is a filepath, renames the copy
shutil.copytree(src, dst) — copies an entire folder tree to a new destination folder (destination must not already exist)

Example:

import shutil
from pathlib import Path
h = Path.home()

shutil.copy(h / 'spam/file1.txt', h)                    # copy to folder, keep name
shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt') # copy and rename

shutil.copytree(h / 'spam', h / 'spam_backup')          # copy entire folder
Gotcha: shutil.copytree() will fail if the destination folder already exists — it creates a brand new folder,
it doesnt merge into an existing one.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
shutil.move() — Moving and Renaming Files

What it is: shutil.move() moves a file or folder to a new location and returns the new path as a string.
If the destination is an existing folder, the file moves into it with its original name.
If the destination path doesnt exist as a folder, the file is moved and renamed to that path.
Why it matters: Handles both moving and renaming in a single function, which is how most file reorganization tasks work in practice.

Example:

shutil.move(h / 'spam/file1.txt', h / 'spam2')              # moves, keeps name
shutil.move(h / 'spam/file1.txt', h / 'spam2/new_name.txt') # moves and renames
Gotcha: If a file with the same name already exists at the destination, shutil.move() silently overwrites it — theres no warning.

Deleting Files and Folders — os.unlink(), os.rmdir(), shutil.rmtree()
What it is: Three functions handle permanent deletion at different scopes — single files, empty folders, and entire folder trees. All deletions are immediate and permanent with no recycle bin involvement.
Why it matters: Lets your program clean up temporary or processed files automatically.
Functions at a glance:

os.unlink(path) — permanently deletes a single file
os.rmdir(path) — deletes a single empty folder only
shutil.rmtree(path) — permanently deletes a folder and everything inside it

Example:
pythonimport os, shutil
from pathlib import Path

# Always do a dry run first — comment out the delete, print instead
for f in Path.home().glob('*.txt'):
    # os.unlink(f)        # uncomment only after confirming output is correct
    print('Would delete:', f)

shutil.rmtree(Path.home() / 'old_folder')   # deletes folder and all contents
Gotcha: These deletions are permanent — always do a dry run by commenting out the delete call and printing filenames first.
A one-character typo in your glob pattern can wipe the wrong files entirely.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

send2trash — Safe Deletion via Recycle Bin
What it is: The third-party send2trash module moves files and folders to the system recycle bin instead of deleting them outright.
It requires installation (pip install send2trash) and is a direct safer replacement for os.unlink() and shutil.rmtree().

Why it matters: Gives you a recovery path if your program deletes something by mistake — the file is still in the bin until you empty it.

Example:

import send2trash

send2trash.send2trash('file1.txt')             # sends to recycle bin
send2trash.send2trash('old_folder')            # works on folders too
Gotcha: Sending to the recycle bin does not free up disk space until the bin is manually emptied —
use permanent deletion only when reclaiming storage is the goal.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

os.walk() — Walking an Entire Directory Tree
What it is: os.walk() lets you loop through every folder and subfolder in a directory tree,
one level at a time. On each iteration it yields three values: the current folder path,
a list of its subfolders, and a list of its filenames.

Why it matters: Without it, processing files in nested subfolders requires complicated recursive code —
os.walk() handles the traversal automatically.
Example:

import os
from pathlib import Path

for folder_name, subfolders, filenames in os.walk(Path.home() / 'spam'):
    print('Folder:', folder_name)
    for filename in filenames:
        print('  File:', filename)
        # Example: rename each file to uppercase
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())

Gotcha: filenames contains only the bare filename strings, not full paths —
you must combine them with folder_name using Path(folder_name) / filename to get a usable path.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
zipfile — Creating and Reading ZIP Archives
What it is: The zipfile module lets you create, read, and extract .zip files from Python.
You open a ZipFile object similar to how you open a regular file —
with a mode of 'w' to create, 'a' to append, or 'r' (default) to read.

Why it matters: Lets your program package and compress multiple files into a single archive,
useful for backups, transfers, or any batch file operation.
Functions/methods at a glance:

zipfile.ZipFile(name, mode) — opens or creates a ZIP archive; use with a with statement
.write(filepath, compress_type) — adds a file to the ZIP with optional compression
.namelist() — returns a list of all filenames inside the ZIP
.getinfo(name) — returns a ZipInfo object with .file_size and .compress_size for one file
.extractall(dest) — extracts all files to the current directory or a specified folder
.extract(name, dest) — extracts a single file

Example:

import zipfile

# Create
with zipfile.ZipFile('backup.zip', 'w') as zf:
    zf.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)

# Read
with zipfile.ZipFile('backup.zip') as zf:
    print(zf.namelist())                         # ['file1.txt']
    info = zf.getinfo('file1.txt')
    print(info.file_size, info.compress_size)    # original vs compressed bytes

# Extract
with zipfile.ZipFile('backup.zip') as zf:
    zf.extractall('output_folder')               # extracts all to folder
    zf.extract('file1.txt', 'output_folder')     # extracts one file
Gotcha: Opening a ZIP in 'w' mode erases its existing contents —
use 'a' to add files to an existing archive without destroying whats already there.
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
Summary:

shutil.copy() / shutil.copytree() copy a single file or full folder tree; shutil.move() moves or renames in one call
os.unlink() deletes a file, os.rmdir() deletes an empty folder, shutil.rmtree() deletes a full folder tree — all permanent, no undo
Always dry run destructive operations first — comment out the delete and print filenames to verify before uncommitting
Use send2trash over permanent deletion whenever recovery might be needed
os.walk() iterates through an entire folder tree yielding (folder, subfolders, filenames) — combine folder_name with filename to get a full path
zipfile.ZipFile() creates, reads, and extracts ZIP archives; use ZIP_DEFLATED for compression; 'w' overwrites, 'a' appends
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
