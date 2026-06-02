'''
Section 5: File I/O (Ch 10)
Test: Build this in 20 minutes:
Build a note saver:
- Add notes with a title
- Save all notes to a JSON file
- Load notes on startup
- View all notes
- Delete a note by title
Pass: File operations feel natural, handles missing file gracefully
Fail: Confusion about open modes, JSON methods
'''
from pathlib import Path
import json

file_dir = Path.home() / ('Exam5')
file_dir.mkdir(parents=True, exist_ok=True)
file_path = file_dir / 'EX5Notes.json'

if file_path.exists():
    EX5Notes = json.loads(file_path.read_text())
else:
    EX5Notes = {}

def add_note(EX5Notes):
    while True:
        title = input("Enter Title of New Note\n")
        if title in EX5Notes:
            print('already a note by that title, try again')
            continue
        note_body = input(f"Type the note titled \n{title}\n")
        EX5Notes[title] = note_body
        print('Note saved succsesfully')
        break
    return

def view_all(EX5Notes):
    if not EX5Notes:
        print('No notes made yet')
    else:
        for Title, Note in EX5Notes.items():
            print(f'\n{Title}\n{Note}\n\n')
    return

def save_exit():
    file_path.write_text(json.dumps(EX5Notes))
    print('Saved')

def remove_note(EX5Notes):
    for title in EX5Notes.keys():
        print(f'{title}')
    note = input('\nEnter Title of the Note to remove: ')
    if note in EX5Notes:
       del EX5Notes[note]
       print(f'{note} removed')
       return
    else:
        print ('Not Found')
        return


while True:
    try:
        choice = int(input("""Note Saver
    would you like to
    1 add Note
    2 remove Note
    3 view all
    9 quit
    """))
        if choice == 1:
            add_note(EX5Notes)
            continue
        elif choice == 2:
            remove_note(EX5Notes)
            continue
        elif choice == 3:
            view_all(EX5Notes)
            continue
        elif choice == 9:
            save_exit()
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue




#
#content = file_path.read_text()
#EX5Notes = json.loads(content)



















