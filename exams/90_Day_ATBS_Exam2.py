'''
Section 2: Data Structures (Ch 5-7)
Test: Build this in 30 minutes:
Build a simple inventory:
- Dictionary of items with quantities
- Add item, remove item, restock, view all
- Warn when stock below 5
- Save to JSON file, load on startup
Pass: Built it, file saves/loads, works correctly
Fail: Struggled with dictionary methods or file I/O
'''
Soft Pass


from pathlib import Path
import json

if file_path.exists():
    EX2GL = json.loads(file_path.read_text())
else:
    EX2GL = {}

file_dir = Path.home() / ('Exam2')
file_path = file_dir / 'EX2GL.json'
file_dir.mkdir(parents=True, exist_ok=True)
#file_path.write_text(json.dumps(EX2GL))
content = file_path.read_text()
EX2GL = json.loads(content)

#loaded_list
def add_item(EX2GL):
    new_item = input('Enter item name to add: ')
    if new_item in EX2GL:
        print('item already in list')
        return
    amount = int(input('enter the amount'))
    EX2GL[new_item] = amount
    print(f"{new_item} added with {amount} in stock")
    return

def remove_item(EX2GL):
    item = input('Enter item name to remove')
    if item in EX2GL:
       del EX2GL[item]
       print(f'{item} removed')
       return
    else:
        print ('Not Found')
        return

def restock_item(EX2GL):
    for item in EX2GL:
       print(f'{item}, {EX2GL[item]}')
    choice = input('enter name of item to restock: ')
    if choice in EX2GL:
        amount = int(input("Enter the amount: "))
        EX2GL[choice] += amount
        print(f"{choice} restocked new Total {EX2GL[choice]}")
        return
    else:
        print('Not Found')
        return


def view_all(EX2GL):
    for item, qty in EX2GL.items():
        if qty < 5:
            print(f'{item}: {qty} — LOW STOCK')
        else:
            print(f'{item}: {qty}')


def save_exit():
    file_path.write_text(json.dumps(EX2GL))
    print('Saved')

while True:
    try:
        choice = int(input("""Grocery list
    would you like to
    1 add item
    2 remove item
    3 restock
    4 view all
    9 quit
    """))
        if choice == 1:
            add_item(EX2GL)
            continue
        elif choice == 2:
            remove_item(EX2GL)
            continue
        elif choice == 3:
            restock_item(EX2GL)
            continue
        elif choice == 4:
            view_all(EX2GL)
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












