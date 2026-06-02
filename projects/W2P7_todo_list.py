'''
W2P7 — To-Do List W2P7_todo_list.py
Menu driven to-do list.
Options: add task, mark complete, view pending, view completed, delete task, quit.
Store tasks as a list of dictionaries with name and status.
'''
import random

to_do = [
{'task': 'clean', 'status' : 'pending'},
{'task': 'cook', 'status' : 'completed'},
{'task': 'laundry', 'status' : 'pending'},
{'task': 'exercise', 'status' : 'pending'}
]

def find_task(task_name):
    for item in to_do:
        if item['task'] == task_name:
            return item
    return None

def add_task():
    task_name = input('Add a task: ').lower()
    if find_task(task_name) is not None:
        print('already exists')
        return
    to_do.append({'task': task_name, 'status': 'pending'})
    print(f'{task_name} added')

def mark_complete():
    task_name = input('Which task is done: ').lower()
    task = find_task(task_name)
    if task is None:
        print(f'{task_name}not found')
        return
    if task['status'] == 'completed':
        print('already done')
        return
    confirm = input('are you sure yes/no: ')
    if confirm != 'yes':
        return
    task['status'] = 'completed'
    print(f'{task_name} completed')

def view_pending():
    pending = [item['task'] for item in to_do if item['status'] == 'pending']#needs practice
    if not pending:
        print('no pending tasks')
        return
    for task in pending:
        print(task)

def view_completed():
    completed = [item['task'] for item in to_do if item['status'] == 'completed']#needs practice
    if not completed:
        print('no completed tasks')
        return
    for task in completed:
        print(task)

def delete_task():
    task_name = input('enter a task to delete: ').lower()
    task = find_task(task_name)
    if task is None:
        print('not found')
        return
    confirm = input('are you sure yes/no: ')
    if confirm != 'yes': return
    to_do.remove(task)
    print(f'{task} deleted')

def random_task():
    pending = [item for item in to_do if item['status'] == 'pending']#needs practice
    if not pending:
        print('all done')
        return
    task = random.choice(pending)
    print (f'how about: {task["task"]}')

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
        elif choice == 9:
            print("you may quit but the tasks still need doing")
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue










