'''
M1P7 — CSV Log / Tracker (Ch 18)
A workout or habit log. Add an entry (date, activity, notes).
View all entries. Filter by date range or activity type. Reads and writes a CSV file. Data persists between runs.
'''
from pathlib import Path
import csv,datetime,os

now = datetime.datetime.now()
time_date = now.strftime("%m-%d-%Y")
print(time_date)

data_dir = Path.home() / 'projects' / 'CH18ATBS'
data_dir.mkdir(parents=True, exist_ok=True)
os.chdir(data_dir)
file = 'M1P7CSVlogTracker.csv'
file_path = data_dir / file


fieldnames = ['date', 'activity', 'notes']
all_rows = []
if file_path.exists():
    with open(file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)

def time_pick():
    return time_date

def all_prev_activitys(all_rows):
    prev_activities = list(set(row['activity'] for row in all_rows))
    return prev_activities

def choice_helper(listacle):
    choice = []
    for num, item in enumerate(listacle, 1):
        print(f'[{num}]. {item}')
        choice.append(item)
    while True:
        try:
            value = choice[int(input('enter the number to select it\n'))-1]
        except ValueError:
            print('invalid choice made try again')
            continue
        except IndexError:
            print('Invalid selection')
            continue
        return value

def add_entry():
    prev_act = all_prev_activitys(all_rows)
    activity = choice_helper(prev_act + ['new'])
    if activity == 'new':
        activity = input('enter the activity:\n').strip().title()
        if activity in prev_act:
            print('already an activity by that name')
            return
    date = time_pick()
    notes = input('enter any notes: ')
    save_entry({'date': date, 'activity': activity, 'notes': notes})
    return

def view_all(all_rows):
    for row in all_rows:
        print('Date'.ljust(9,' '),row['date'],'\nActivity'.ljust(10,' '),row['activity'],'\nNotes:\n',row['notes'])

def filter_by_activity(all_rows):
    matched_rows = []
    unique_act = all_prev_activitys(all_rows)
    print('Choose which activity you want to see')
    activity = choice_helper(unique_act)
    with open(file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['activity'] == activity:
                matched_rows.append(row)
    for row in matched_rows:
        print('Date'.ljust(9,' '),row['date'],'\nActivity'.ljust(10,' '),row['activity'],'\nNotes:\n',row['notes'])

def vali_date(variable):
    while True:
        try:
            user_date = input(f"enter the {variable} date in MM-DD-YYYY format or '0' (Zero) to exit\n").strip().lower()
            if user_date == '0':
                return False
            user_date = strp_time(user_date)
        except ValueError:
            print(f'requires exact format ex. {now.month}-{now.day}-{now.year}')
            continue
        break
    return user_date

def strp_time(time):
    return datetime.datetime.strptime(time, '%m-%d-%Y')

def filter_by_date_range():
    print('To see what was logged between 2 dates')
    start_date = vali_date('1st')
    if start_date == False:
        print('Exiting')
        return
    end_date = vali_date('2nd')
    if end_date == False:
        print('Exiting')
        return
    if start_date > end_date:
        print("the first date needs to be older then the second date\nTry again")
        return
    matched_rows = []
    with open(file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if strp_time(row['date']) > start_date:
                if strp_time(row['date']) < end_date:
                    matched_rows.append(row)
    for row in matched_rows:
        print('Date'.ljust(9,' '),row['date'],'\nActivity'.ljust(10,' '),row['activity'],'\nNotes:\n',row['notes'])


def save_entry(row):
    all_rows.append(row)
    file_exists = file_path.exists()
    with open(file, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    print('entry saved')

menu_options = ['Add entry','View all','Filter by Activity','Filter by Date','Quit']

def main_menu():
    while True:
        print('*'*5,'Main menu','*'*5)
        for i, item in enumerate(menu_options,1):
            print(i,item)
        choice = input('\nEnter a number: ').strip()
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_all(all_rows)
        elif choice == '3':
            filter_by_activity(all_rows)
        elif choice == '4':
            filter_by_date_range()
        elif choice == '5':
            print('Goodbye.')
            break
        else:
            print('Invalid choice — enter 1, 2, 3, 4 or 5.')

main_menu()



