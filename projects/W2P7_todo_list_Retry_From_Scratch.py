'''
To-Do List W2P7
Menu driven to-do list.
Options:
add task, mark complete, view pending, view completed, delete task, quit.
Store tasks as a list of dictionaries with name and status.
'''
import random

to_do = [
{'task': 'clean', 'status' : 'pending','priority':'low'},
{'task': 'cook', 'status' : 'completed','priority':'high'},
{'task': 'laundry', 'status' : 'pending','priority':'low'},
{'task': 'exercise', 'status' : 'pending','priority':'high'}
]

def find_task(task_name):
    for item in to_do:
        if item['task'] == task_name:
            return item
    return None

def add_task():
    task_name = input('Add task name: ').lower()
    check_list = find_task(task_name)
    if check_list is not None:
        print('item Already Added')
        return
    priority = input('priority level High/Low: ').lower()
    if priority not in ['high','low']:
        print('invalid priority level')
        return
    to_do.append({'task': task_name, 'status' : 'pending','priority': priority})
    print ('task added')
    return

def mark_complete():
    to_do_pending = [item for item in to_do if item['status'] == 'pending']
    for i in range(len(to_do_pending)):
        index = i + 1
        items = to_do_pending[i]['task']
        print(index,items)
    try:
        update_status = int(input('which item was completed enter its #: ')) -1
        selected = to_do_pending[update_status]
        selected['status'] = 'completed'
        print (f"{selected['task']} completed")
    except ValueError:
        print('invalid input')
        return
    except IndexError:
        print('invalid input')
        return

def confirm_choice():
    choice = input("are you sure? yes/no: ").lower()
    if choice == 'yes':
        return True
    return False

def view_pending():
    print('Pending tasks:')
    pending = [item for item in to_do if item['status'] == 'pending']
    for i in pending:
        print(f"{i['task']}, Still Pending")
    return

def view_completed():
    print('Completed tasks:')
    completed = [item for item in to_do if item['status'] == 'completed']
    for i in completed:
        print(i['task'])
    return

def view_priority():
    choice = input('High/Low: ').lower()
    if choice not in ['high','low']:
        print('invalid input')
        return
    H_or_L = [item for item in to_do if item['priority'] == choice ]
    print(f"Tasks with {choice} priority are")
    for item in H_or_L:
        print(item['task'])
    return

def delete_task():
    for i in range(len(to_do)):
        index = i + 1
        items = to_do[i]
        print(f"{index}: {items['task'].ljust(5)}{items['status'].rjust(10)}")
    try:
        remove_me = int(input('enter The Number to the left of the item to remove it: ')) -1
        selected = to_do[remove_me]
        DBL_check = confirm_choice()
        if DBL_check is False:
            print('Nothing was removed')
            return
        to_do.remove(selected)
        print (f"{selected['task']} has been removed")
        return
    except ValueError:
        print('invalid input')
        return
    except IndexError:
        print('invalid input')
        return

def random_task():
    pending = [item for item in to_do if item['status'] == 'pending']
    if not pending:
        print('no pending tasks')
        return
    do_now = random.choice(pending)
    print(f"{do_now['task']} Priority level {do_now['priority']}\n")
    return

while True:
    try:
        choice = int(input("""Your To Do list.
    would you like to
    1.Add Task
    2.Mark a Task Completed
    3.View Pending Tasks
    4.View Completed Tasks
    5.Delete a Task
    6.Random Task
    7.View Task by priority
    9.Quit
    """))
        if choice == 1:
            add_task()
            continue
        elif choice == 2:
            mark_complete()
            continue
        elif choice == 3:
            view_pending()
            continue
        elif choice == 4:
            view_completed()
            continue
        elif choice == 5:
            delete_task()
            continue
        elif choice == 6:
            random_task()
        elif choice == 7:
            view_priority()
        elif choice == 9:
            print("you may quit but the tasks still need doing")
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue














































































