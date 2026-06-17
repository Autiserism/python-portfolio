'''
M1P4 — Scheduled Task Reminder (Ch 19)
Add a task with a name and due date. View all tasks.
When the program runs it automatically flags any overdue tasks.
Tasks sorted by due date. Saved to JSON so nothing is lost between runs.
'''
from pathlib import Path
import time,datetime,json,random #,re

data_dir = Path.home() / 'projects'
data_dir.mkdir(parents=True,exist_ok=True)
file_path = data_dir / 'Task_Reminder.json'

if file_path.exists() and file_path.is_file():
    STR = json.loads(file_path.read_text())
else:
    STR = {}

now = datetime.datetime.now()
_ = False

"""       All Helper Functions          """

def vali_date(variable,name):
    while True:
        try:
            user_date = input(f"enter {name}(s) {variable} date in MM/DD/YYYY format or '0' (Zero) to exit\n").strip().lower()#f'07/17/2026'#
            if user_date == '0':
                return False
            if datetime.datetime.strptime(user_date, '%m/%d/%Y') < now:
                print('you\'re not a time traviler and cant schedule events in the past')
                continue
        except ValueError:
            print(f'requires exact format ex. {now.month}/{now.day}/{now.year}')
            continue
        break
    return user_date

def confirmation_check(task_name, english_date, date):
    while True:
        if not english_date and not date:
            confirm_choice = input(f"type 'yes' to confirm '{task_name}'\nOr '0' to exit\n").strip().lower()
        if english_date and date:
            confirm_choice = input(f"type 'yes' to confirm that \n\n{task_name} is due on {english_date} ({date})\n\nOr '0' (Zero) to exit\n").strip().lower()
        if confirm_choice == '0':
            print('Exiting')
            return False
        if confirm_choice != 'yes':
            print ('invalid input try again')
            continue
        break
    return True

def proper_datetime(date):
    date = datetime.datetime.strptime(date, '%m/%d/%Y')
    return date

def fetch_english_date(task_variable):
    task_variable = datetime.datetime.strptime(task_variable, '%m/%d/%Y')
    return task_variable.strftime('%A, %B %d %Y')

def select_task(note):
    if not STR:
        print('No tasks to modify\Return when you have something to do')
        return
    print(f'First select a task {note}')
    picked = verify_choice()
    if picked == 'quit':
        print('no changes made')
        return
    english_date = fetch_english_date(STR[picked])
    print(f"The current due date for {picked} is on {english_date} ({STR[picked]})")
    return picked

def verify_choice():
    quick_pick = ['quit']
    for i,task in enumerate(STR,1):
        print (i,task)
        quick_pick.append(task)
    while True:
        try:
            choice = int(input('\nenter the number to the left of the task name to select it or: 0 (Zero) to exit\n'))
            return quick_pick[choice]
        except ValueError:
            print("invalid input")
            continue
        except IndexError:
            print("wrong selection")
            continue

"""     All Task Menu Options        """

def overdue_tasks():
    overdue = []
    for name in STR:
        if proper_datetime(STR[name]) < now:
            print(name,'overdue', STR[name])
            overdue.append(name)
    print(''.rjust(40,'='))
    while True:
        if not overdue:
            print('no tasks overdue')
            return
        if overdue:
            print(f"You have {len(overdue)} tasks overdue")
        for name in overdue:
            failsafe = False
            while failsafe == False:
                print(f"\n{name} has expired on {STR[name]}\n")
                choice =input('Would you like to:\n1 Delete the task\n2 Change the due date\n')
                if choice not in ['1','2']:
                    print('invalid input')
                    continue
                if choice == '1':
                    delete_task(name)
                    overdue.remove(name)
                    break
                if choice == '2':
                    failsafe = update_a_due_date(name)
                    if failsafe:
                        overdue.remove(name)
                    else:
                        print ('\ntask still needs attention')
                        continue
                break

def add_task():
    new_task = input("enter the name of the task you want to add\n")
    task_date = vali_date('due', new_task)
    if not task_date:
        print("Add task canceled")
        return
    english_date = fetch_english_date(task_date)
    confirm_choice = confirmation_check(new_task,english_date,task_date)
    if not confirm_choice:
        print('Nothing was added')
        return
    STR[new_task] = task_date
    print(f"{new_task} added to tasks due on {english_date} ({task_date})")
    return

def update_a_task_name():
    picked = select_task('name to update')
    new_name = input(f"enter the name that will be replacing {picked}\n")
    confirm = confirmation_check(new_name, _, _)
    if not confirm:
        print('Nothing was changed')
        return False
    STR[new_name] = STR.pop(picked)
    print("task name updated succsesfully")
    return

def update_a_due_date(picked):
    if not picked:
        picked = select_task('that you need to change the date for')
    new_date = vali_date('updated',picked)
    if not new_date:
        print('Date Update canceled')
        return False
    if new_date == STR[picked]:
        print('it was already due that day')
        return
    english_date = fetch_english_date(new_date)
    choice = confirmation_check(picked, english_date, new_date)
    if not choice:
        print('Nothing was changed')
        return False
    STR[picked] = new_date
    print(f"{picked}, due date updated to {english_date} ({STR[picked]})")
    return True

def delete_task(picked):
    if not picked:
        picked = select_task('that you want to delete')
        print(f"preparing to delete {picked} due on {STR[picked]}")
        confirm = confirmation_check(picked, _, _)
        if not confirm:
            print('Nothing was deleted')
            return False
    STR.pop(picked, None)
    print(f"{picked} succsesfully deleted")
    return

def view_all_tasks():
    for num, name in enumerate(STR, 1):
        print(f"{num}. {name}, due on {fetch_english_date(STR[name])} ({STR[name]})")

def sort_by_due():
    close_to_far = sorted(STR.items(),key=lambda x: datetime.datetime.strptime(x[1], '%m/%d/%Y'))
    for name, date in close_to_far:
        print(f"{date} - {name}")

def save_quit():
    file_path.write_text(json.dumps(STR))
    print('tasks saved succsesfully')

overdue_tasks()

while True:
    try:
        choice = int(input("""Scheduled Task Reminder
    would you like to
    1. Add a Task
    2. See what tasks are due next
    3. View all tasks
    4. Delete a task
    5. Change a due date on a Task
    6. Change a task name
    7. Save & Quit
    8. Refresh tasks

    9. Quit
    """))
        if choice == 1:
            add_task()
            continue
        elif choice == 2:
            sort_by_due()
            continue
        elif choice == 3:
            view_all_tasks()
            continue
        elif choice == 4:
            delete_task(_)
            continue
        elif choice == 5:
            update_a_due_date(_)
            continue
        elif choice == 6:
            update_a_task_name()
            continue
        elif choice == 7:
            save_quit()
            continue
        elif choice == 8:
            overdue_tasks()
            continue
        elif choice == 9:
            if input('Save before quitting? yes/no: ') == 'yes':
                save_quit()
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue



















