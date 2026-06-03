'''
Drill 3 — Dictionary as a database
Write a program that stores student records as a dictionary
where the key is student ID and the value is a dictionary with name, grade and score.
Write functions to add a record, look up by ID, update a score and delete a record.
Use try/except to handle missing IDs.
'''

database = {
    '0024': {'name': 'Gman', 'grade': 'C', 'score': 72},
    '0055': {'name': 'Bob', 'grade': 'B', 'score': 88},
    '0043': {'name': 'Candace', 'grade': 'B', 'score': 80}
}

def add_record(database):
    new_id = input('enter students 4 Digit ID: ')
    if new_id in database:
        print("student already exists")
        return
    name = input('enter their name: ')
    score = int(input('enter their score 0-100: '))
    grade = 'A' if score >=90 else 'B' if score >=80 else 'C' if score >=70 else 'F'
    database[new_id] = {'name': name, 'grade' : grade, 'score' : score}
    print(f"{name} has been added to the database")
    return

def look_up_id (database):
    lookup = input('enter a students id: ')
    if lookup in database:
        stats = database[lookup]
        print(f"{stats['name']} {stats['grade']}")
        return
    else:
        print(f'{lookup} is not in the database')
        return

def update_score(database):
    student_id = input("Enter the students id you wish to update: ")
    if student_id not in database:
        print("enter a valid students id")
        return
    stats = database[student_id]
    try:
        new_score = int(input(f"Enter {stats['name']}'s new 0-100 score: "))
    except ValueError:
        print("invalid has to be a number from 0-100")
        return
    grade = 'A' if new_score >= 90 else 'B' if new_score >= 80 else 'C' if new_score >= 70 else 'F'
    database[student_id]['score'] = new_score
    database[student_id]['grade'] = grade
    print(f"{stats['name']} score has been updated to {new_score} \nNew grade is {grade}")
    return

def delete_record(database):
    choice = input("Enter the Student ID you wish to delete: ")
    if choice not in database:
        print('Student not found')
        return
    stats = database[choice]
    del database[choice]
    print(f"{stats['name']} has been removed")


def view_all(database):
    if not database:
        print('empty')
    for student_id, stats in database.items():
        print(f"{student_id} {stats['name']} {stats['grade']}\n")
    return


while True:
    print("""Options
    1. Add A Record
    2. Look up by ID
    3. Update a score
    4. Delete a record
    5. View All
    9. To Quit""")
    try:
        choice = int(input('> '))
    except ValueError:
        print('\nEnter a valid selection')
        continue
    if choice == 1:
        add_record(database)
    elif choice == 2:
        look_up_id(database)
    elif choice == 3:
        update_score(database)
    elif choice == 4:
        delete_record(database)
    elif choice == 5:
        view_all(database)
    elif choice == 9:
        break
    else:
        print('Pick from one of the options')



























