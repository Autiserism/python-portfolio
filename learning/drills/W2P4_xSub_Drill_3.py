'''
Drill 3 — Dictionary as a database
Write a program that stores student records as a dictionary
where the key is student ID and the value is a dictionary with name, grade and score.
Write functions to add a record, look up by ID, update a score and delete a record.
Use try/except to handle missing IDs.
'''

database = {  # Create the main dictionary that stores all student records.
    '0024': {'name': 'Gman', 'grade': 'B+', 'score': 72},  # Student ID 0024 points to Gman's record.
    '0055': {'name': 'Bob', 'grade': 'A', 'score': 88},  # Student ID 0055 points to Bob's record.
    '0043': {'name': 'Candace', 'grade': 'A-', 'score': 80}  # Student ID 0043 points to Candace's record.
}  # End of the starting database.

def add_record(database):  # Define a function that adds a new student record to the database.
    student_id = input('Enter 4 digit ID: ')  # Ask the user for the new student's ID.
    if student_id in database:  # Check if that ID is already being used.
        print('ID already exists')  # Tell the user the ID cannot be reused.
        return  # Stop this function early so we do not overwrite an existing record.
    name = input('Enter name: ')  # Ask the user for the student's name.
    score = int(input('Enter score 0-100: '))  # Ask for score and convert it from text to an integer.
    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'  # Choose grade based on score.
    database[student_id] = {'name': name, 'grade': grade, 'score': score}  # Add the new student dictionary under their ID.
    print(f'{name} added successfully')  # Confirm the student was added.


def lookup_id(database):  # Define a function that finds and displays one student by ID.
    student_id = input('Enter student ID: ')  # Ask the user which student ID to search for.
    if student_id not in database:  # Check if the ID does not exist.
        print('ID not found')  # Tell the user no matching record was found.
        return  # Stop this function early because there is nothing to display.
    info = database[student_id]  # Get the inner dictionary for that student and save it as info.
    print(f"\nID: {student_id}")  # Print the student's ID.
    print(f"Name: {info['name']}")  # Print the student's name from the inner dictionary.
    print(f"Grade: {info['grade']}")  # Print the student's grade from the inner dictionary.
    print(f"Score: {info['score']}")  # Print the student's score from the inner dictionary.


def update_score(database):  # Define a function that updates a student's score and grade.
    student_id = input('Enter student ID to update: ')  # Ask which student ID should be updated.
    if student_id not in database:  # Check if the ID is missing from the database.
        print('ID not found')  # Tell the user the student does not exist.
        return  # Stop this function early because we cannot update a missing record.
    try:  # Start a protected block in case the user enters invalid number text.
        new_score = int(input('Enter new score 0-100: '))  # Ask for new score and convert it to an integer.
    except ValueError:  # Run this block if int(...) fails, like if the user types "abc".
        print('Invalid score')  # Tell the user the score was not valid.
        return  # Stop this function early because we do not have a usable score.
    database[student_id]['score'] = new_score  # Replace the old score with the new score.
    database[student_id]['grade'] = 'A' if new_score >= 90 else 'B' if new_score >= 80 else 'C' if new_score >= 70 else 'F'
    # Recalculate grade from the new score.
    print(f"Score updated to {new_score}")  # Confirm the update worked.


def delete_record(database):  # Define a function that deletes a student record.
    student_id = input('Enter student ID to delete: ')  # Ask which student ID should be deleted.
    if student_id not in database:  # Check if that ID is not in the database.
        print('ID not found')  # Tell the user there is no record to delete.
        return  # Stop this function early.
    name = database[student_id]['name']  # Save the student's name before deleting the record.
    del database[student_id]  # Delete the student ID and its inner dictionary from the database.
    print(f'{name} deleted')  # Confirm which student was deleted.

def view_all(database):  # Define a function that displays every student record.
    if not database:  # Check if the database is empty.
        print('No records')  # Tell the user there are no records.
        return  # Stop this function early because there is nothing to print.
    for student_id, info in database.items():  # Loop through each ID and student-info dictionary in the database.
        print(f"\nID: {student_id}")  # Print the current student's ID.
        print(f"  Name: {info['name']}")  # Print the current student's name.
        print(f"  Grade: {info['grade']}")  # Print the current student's grade.
        print(f"  Score: {info['score']}")  # Print the current student's score.

while True:  # Start an infinite loop so the menu keeps showing until the user quits.
    print('''
Student Database
1 Add record
2 Lookup by ID
3 Update score
4 Delete record
5 View all
9 Quit''')  # Print the menu options.
    choice = input('> ')  # Ask the user to choose a menu option.
    if choice == '1':  # If the user chose option 1...
        add_record(database)  # Call the function that adds a new student.
    elif choice == '2':  # If the user chose option 2...
        lookup_id(database)  # Call the function that looks up one student by ID.
    elif choice == '3':  # If the user chose option 3...
        update_score(database)  # Call the function that updates a student's score.
    elif choice == '4':  # If the user chose option 4...
        delete_record(database)  # Call the function that deletes a student.
    elif choice == '5':  # If the user chose option 5...
        view_all(database)  # Call the function that displays all students.
    elif choice == '9':  # If the user chose option 9...
        break  # Exit the while loop, which ends the program.
    else:  # If the user typed anything other than the valid menu choices...
        print('Invalid choice')  # Tell the user their choice was not valid.

'''

database = {
    '0024': {'name': 'Gman', 'grade': 'B+', 'score': 72},
    '0055': {'name': 'Bob', 'grade': 'A', 'score': 88},
    '0043': {'name': 'Candace', 'grade': 'A-', 'score': 80}
}

def add_record(database):
    student_id = input('Enter 4 digit ID: ')
    if student_id in database:
        print('ID already exists')
        return
    name = input('Enter name: ')
    score = int(input('Enter score 0-100: '))
    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
    database[student_id] = {'name': name, 'grade': grade, 'score': score}
    print(f'{name} added successfully')

def lookup_id(database):
    student_id = input('Enter student ID: ')
    if student_id not in database:
        print('ID not found')
        return
    info = database[student_id]
    print(f"\nID: {student_id}")
    print(f"Name: {info['name']}")
    print(f"Grade: {info['grade']}")
    print(f"Score: {info['score']}")

def update_score(database):
    student_id = input('Enter student ID to update: ')
    if student_id not in database:
        print('ID not found')
        return
    try:
        new_score = int(input('Enter new score 0-100: '))
    except ValueError:
        print('Invalid score')
        return
    database[student_id]['score'] = new_score
    database[student_id]['grade'] = 'A' if new_score >= 90 else 'B' if new_score >= 80 else 'C' if new_score >= 70 else 'F'
    print(f"Score updated to {new_score}")

def delete_record(database):
    student_id = input('Enter student ID to delete: ')
    if student_id not in database:
        print('ID not found')
        return
    name = database[student_id]['name']
    del database[student_id]
    print(f'{name} deleted')

def view_all(database):
    if not database:
        print('No records')
        return
    for student_id, info in database.items():
        print(f"\nID: {student_id}")
        print(f"  Name: {info['name']}")
        print(f"  Grade: {info['grade']}")
        print(f"  Score: {info['score']}")

while True:
    print(#'"''
Student Database
1 Add record
2 Lookup by ID
3 Update score
4 Delete record
5 View all
9 Quit)#'"''
    choice = input('> ')
    if choice == '1':
        add_record(database)
    elif choice == '2':
        lookup_id(database)
    elif choice == '3':
        update_score(database)
    elif choice == '4':
        delete_record(database)
    elif choice == '5':
        view_all(database)
    elif choice == '9':
        break
    else:
        print('Invalid choice')

'''



