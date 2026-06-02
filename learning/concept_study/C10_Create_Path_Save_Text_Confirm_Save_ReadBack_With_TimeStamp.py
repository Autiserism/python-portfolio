'''
Drill 3
Write a program that:

Asks the user to type a note
Appends it to a file called journal.txt in your home directory with a timestamp on each entry
After saving prints "Note saved"
Then reads the entire file back and prints all previous entries

Use open() with append mode 'a' and with open() as f: syntax for this one — good habit for file handling.
'''
from pathlib import Path
import os
import datetime

save_path = Path.home()
folder = save_path / 'projects'
os.makedirs(folder,exist_ok=True)

journal = folder / 'journal.txt'

with open(journal, 'a', encoding='UTF-8') as f:
    user_text = input('enter note:\n')
    add_date = datetime.datetime.now()
    entry = (f"\n{user_text} {add_date}")
    f.write(entry)
    print('note saved')

print(journal.read_text())















