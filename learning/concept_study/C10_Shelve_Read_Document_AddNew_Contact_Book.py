'''
Drill 4
Write a program that uses shelve to build a simple persistent contact book. The program should:

Load existing contacts from the shelf on startup
Ask if the user wants to add a contact or look one up
Save any new contacts back to the shelf
Contacts should survive closing and reopening the program
'''

from pathlib import Path
import os
import shelve


save_path = Path.home()
folder = save_path / 'projects' / 'contact_book'
os.makedirs(folder, exist_ok=True)
#CB = folder / 'contact_book'
os.chdir(folder)

shelf_file = shelve.open('contacts')
if 'all_contacts' not in shelf_file:
    shelf_file['all_contacts'] = []
print(shelf_file['all_contacts'])

while True:
    choice = int(input("1 add contact \n2 lookup contact\n9 quit\n"))
    if choice == 1:
        new_contact = shelf_file['all_contacts']
        new_contact.append(input("enter name\n"))
        shelf_file['all_contacts'] = new_contact
    if choice == 2:
        person = input('enter name\n')
        if person in shelf_file["all_contacts"]:
            print(shelf_file['all_contacts'])
        else:
            print('not found')
    if choice == 9:
        break

shelf_file.close()















