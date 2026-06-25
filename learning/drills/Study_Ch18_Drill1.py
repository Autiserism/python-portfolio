'''
Drill 1
Write a program that:

Creates a CSV file called contacts.csv with columns: name, phone, email
Writes at least 4 contacts to it
Reads it back using csv.DictReader() and prints each contact formatted cleanly

Remember newline='' when opening on Windows.
'''
import csv , os
from pathlib import Path
data_path = Path.home() / 'projects' / 'CH18ATBS'
data_path.mkdir(parents=True,exist_ok=True)
os.chdir(data_path)

#insert regex verification codeblocks

def add_contact():
    TBW = {}
    TBW['name'] = 'soup'#input('Enter name: ')
    TBW['phone'] = 'ten digits'#input('Enter Phone: ')
    TBW['email']= 'email@email.ca'#input('Enter email: ')
    return TBW

with open('contacts.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email'])
    writer.writeheader()
    for i in range(4):
        writer.writerow(add_contact())

f.close()
print(f"{'*'*10}All contacts{'*'*10}")
with open('contacts.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['phone'], row['email'])













