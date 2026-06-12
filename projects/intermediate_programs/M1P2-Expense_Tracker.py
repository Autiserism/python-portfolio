''''
M1P2 — Expense Tracker
Add an expense (name, amount, category), view all expenses, view total, view by category.
Saves to a JSON file and loads it on startup so data persists between runs.
Menu-driven loop. Input validation.
'''
from pathlib import Path
import json, re

'''
data_dir = Path.home() / 'projects'/ 'M1P2'
data_dir.mkdir(parents=True,exist_ok=True)
file_path = data_dir / 'expenses.json'

if file_path.exists() and file_path.is_file():
    content = json_file.read_text()
    expenses = json.loads(content)
else:
    expenses = {}
'''

expenses = {
'food' : { 'beef' : 40.00 ,'vegetables' : 30.00, 'eggs' : 10.00, 'rice' : 6.00 , 'seasoning' : 4.00},
'subscriptions' : {'gym' : 17.50 , 'Ai' : 10.00, 'other' : 7.50},
'life' : { 'phone' : 20.00, 'car' : 200.00 , 'apartment' : 320.00, 'purchases': 30.00}
}


def new_category():
    while True:
        new_item = input("enter the name of the new category or 'Quit' to exit\n").strip().lower()
        if new_item == 'quit':
            return
        confirm_check = input(f"type 'yes' to confirm and create a new category named: {new_item}\n").strip().lower()
        if confirm_check != 'yes':
            continue
        expenses[new_item] = {}
        break
    return


def add_expense_menu():
    while True:
        tmp = []
        print('Add an expense to a category by entering the number to the left of it ')
        for num,name in enumerate(expenses,1):
            print(num, name)
            tmp.append(name)
        print ("\ntype 'New' for a new catagory\nOr 'Quit' to exit") #
        index = input('make a selection: ').strip().lower()
        if index == 'new':
            new_category()
            print(expenses) #<<<<<<<<<<<<<<<<<<<<<
            continue
        if index == 'quit':
            break
        print('debug > ',tmp) #<<<<<<<<<<<<<<<<<<<<<<<<

        try:
            index = int(index)
            item = tmp[index-1]
            result = add_expense(item)
            if result:
                print(f"Added {result} to {item} expenses")
                break
            else:
                print('nothing was added')
                break
        except ValueError:
            print('invalid input')
            continue
        except IndexError:
            print('invalid number selection')
            continue

def add_expense(item):
    while True:
        new_expense = input(f"\nenter the item name to add to the {item} catagory\n or 'Quit' to exit\n: ").strip().lower()
        if new_expense in expenses[item]:
            print ('item already a part of expenses')
            break
        if new_expense == 'quit':
            break
        if not new_expense:
            print('name cant be blank')
            continue
        confirm_check = input(f"type 'yes' to confirm and create a new weekly cost named: {new_expense}\n").strip().lower()
        if confirm_check != 'yes':
            continue
        amount = round(float(input(f'enter {new_expense}(s) the weekly cost: $')),2)
        expenses[item][new_expense] = amount
        return new_expense
    return None

def view_all_expenses():
    for i, category in enumerate(expenses, 1):
        total = sum(expenses[category].values())
        print(f"\n{i}. {category.title()}")#- Weekly Total: ${total:.2f}
        for item, amount in expenses[category].items():
            print(f"     {item.title()} ${amount:.2f} ")#

def view_total():
    grand_total = []
    time_scale = ['Daily','Weekly','Monthly','Yearly']
    for num, name in enumerate(time_scale, 1):
        print(num, name)
    while True:
        choice = input('Enter the number to the left to select a timeframe: ')
        choice = verify_choice(choice,time_scale)
        if not choice:
            continue
        if choice == 'Daily':#time_scale[choice]
            Y = 0.14285
            break
        if choice == 'Weekly':
            Y = 1
            break
        elif choice == 'Monthly':
            Y = 4
            break
        elif choice == 'Yearly':
            Y = 52
            break
    ranked = sorted(expenses, key=lambda x: sum(expenses[x].values()), reverse=True)
    for i, category in enumerate(ranked, 1):
        total = sum(expenses[category].values())
        grand_total.append(total*Y)
        print(f"\n{i}. {category.title()} — {choice} Total: ${total * Y:.2f}")
        for item, amount in expenses[category].items():
            print(f"     {item.title()}: ${amount * Y:.2f}")
    print(f"Total {choice} cost = ${sum(grand_total):.2f}")

def view_by_catagory():
    view_index = []
    for i, category in enumerate(expenses, 1):
        print(f"{i}. {category.title()}")
        view_index.append(category)
    while True:
        choice = input('Enter the number of the category you want to see: ')
        gather = verify_choice(choice,view_index)
        if not gather:
            continue
        break
    print(f"all items within {gather}")
    for i, item in enumerate(expenses[gather],1):
        print(i,item,' $',expenses[gather][item])

def update_expense():
    progression = 0
    view_index = []
    category_index = []
    for i, category in enumerate(expenses, 1):
        print(f"{i}. {category.title()}")
        view_index.append(category)
    while progression == 0:
        choice = input('First enter the number of the category \nthat the expense you want to update is in\n')
        gather = verify_choice(choice, view_index)
        if not gather:
            continue
        progression +=1
        while progression == 1:
            print('Which item in ',gather)
            for i, sub_category in enumerate(expenses[gather], 1):
                print(f"{i}. {sub_category.title()}: ${expenses[gather][sub_category]}")#- Weekly Total: ${total:.2f}
                category_index.append(sub_category)
            choice = input('') #Enter the number of the category you want to see:
            gather2 = verify_choice(choice,category_index)
            if not gather2:
                continue
            progression +=1
            while True:
                try:
                    new_value = int(input(f'enter the new Weekly cost for {gather2}\n'))
                    if new_value < 0:
                        print('expenses cant be negative')
                        continue
                    progression +=1
                    break
                except ValueError:
                    print('invalid input')
                    continue
    confirm_check = input(f"type 'yes' confirm that {round(new_value)} is the new WEEKLY cost of {gather2}\n").strip().lower()
    progression = 0
    if confirm_check != 'yes':
        print('No Changes Made')
        return
    expenses[gather][gather2] = round(new_value)
    print (f"succsesfully changed the weekly cost of {gather2} to {new_value}")
    return

def verify_choice(choice, index_list):
    try:
        choice = int(choice) - 1
        if not index_list:
            return choice
        variable = index_list[choice]
        return variable
    except ValueError:
            print('invalid input')
            return None
    except IndexError:
        print('Invalid choice')
        return None


#def save_quit():


add_expense_menu()
#view_by_catagory()
#view_total()
#update_expense()
print(expenses)
print('test done')



