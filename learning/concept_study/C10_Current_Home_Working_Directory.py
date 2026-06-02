"""
Drill 1

Write a program that uses Path to:

Print the current working directory
Print your home directory
Build a path to a file called notes.txt
inside a folder called projects inside your home directory
Print each part of that path — stem, suffix, name, parent
"""

from pathlib import Path
import os
print(Path.cwd())
print(Path.home())
note = Path('CH10notes.txt')
#note.write_text('work')
save_path = Path.home()
folder = save_path / 'projects' #New
os.makedirs(folder, exist_ok=True)
file_path = folder / 'CH10notes.txt'#New
p = Path('Users') / 'tylhe' / 'CH10notes.txt'
print(p.parts)
print(p.stem)
print(p.suffix)
print(p.name)
print(p.parent)
'''
os.makedirs(save_path/'projects'/note) treats the file as a folder

makedirs creates directories — passing a path ending in CH10notes.txt
tries to create a folder named CH10notes.txt. Build the folder path separately from the file path:

folder = save_path / 'projects'

os.makedirs(folder, exist_ok=True)  # exist_ok prevents crash if already exists

file_path = folder / 'CH10notes.txt'

p.parts gives a tuple of each piece

Path('Users/tylhe/CH10notes.txt').parts

# ('Users', 'tylhe', 'CH10notes.txt')
useful for understanding path structure.

exist_ok=True is worth always including

Without it makedirs crashes if the folder already exists.
'''







