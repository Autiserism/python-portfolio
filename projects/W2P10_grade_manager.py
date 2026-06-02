'''
W2P10 — Student Grade Manager W2P10_grade_manager.py
Full grade management system.
Add students, add scores per subject, calculate averages, display ranked list.
Store as nested dictionaries. Use logging to track all changes.
'''
import logging
logging.basicConfig(level=logging.DEBUG)

students = [
    {'name': 'Lary', 'average': 88, 'subjects' : {'math' : 90, 'english' : 85, 'gym' : 90} },
    {'name': 'Bob', 'average': 90, 'subjects' : {'math' : 88, 'english' : 90, 'gym' : 92} },
    {'name': 'Sarah', 'average': 73, 'subjects' : {'math' : 75, 'english' : 65, 'gym' : 80} },
    {'name': 'Mike', 'average': 77, 'subjects' : {'math' : 77, 'english' : 88, 'gym' : 67} },
    {'name': 'Jess', 'average': 78, 'subjects' : {'math' : 88, 'english' : 78, 'gym' : 68} },
    {'name': 'Anna', 'average': 85 , 'subjects' : {'math' : 88, 'english' : 77, 'gym' : 92} },
]

def find_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None

def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_average(subjects):
    return sum(subjects.values()) / len(subjects)

def add_student():
    name = input('Enter name: ').title()
    if find_student(name) is not None:
        print('Already exists')
        return
    subjects = {'math' : 00, 'english' : 00, 'gym' : 00}
    for subject in subjects:
        print(f"Enter the score for {subject}")
        subjects[subject] = int(input(': '))
    average = calculate_average(subjects)
    grade = get_grade(average)
    students.append({'name': name, 'average': average, 'grade': grade, 'subjects': subjects})
    logging.debug(f'added {name}')
    print(f"{name} Added")

def update_score():
    name = input("enter students name: ").title()
    student = find_student(name)
    if student is None:
        print('not found')
        return
    print(f"Name: {student['name']}")
    print(f"Math grade: {student['subjects']['math']}")
    print(f"English grade: {student['subjects']['english']}")
    print(f"Gym grade: {student['subjects']['gym']}")
    subject = input('which subject: ').lower()
    if subject not in student['subjects']:
        print('not found')
        return
    try:
        new_score = int(input('new score: '))
        student['subjects'][subject] = new_score
        student['average'] = calculate_average(student['subjects'])
        student['grade'] = get_grade(student['average'])
        logging.debug(f'updated {name} {subject} {new_score}')
        print('score updated succsesfully')
        return
    except ValueError:
        print('invalid input')
        return

def view_student():
    name = input('Enter student name: ').title()
    student = find_student(name)
    if student is None:
        print('not found')
        return
    print(f"{student['name']} \nAverage: {student['average']} \nGrade: {get_grade(student['average'])}")
    for subject, score in student['subjects'].items():
        print(f'Subject: {subject} Score: {score}')

def view_ranked():
    ranked = sorted(students, key=lambda x: x['average'], reverse=True) # wouldent have gotten
    for i, student in enumerate(ranked, 1): # wouldent have gotten
        print (f"{i}. {student['name']} - avg {student['average']} - grade {get_grade(student['average'])}")

def delete_student():
    name = input('Enter Students name: ').title()
    student = find_student(name)
    if student is None:
        print('not found')
        return
    students.remove(student)
    logging.debug(f'deleted {name}')
    print (f'{name} has been removed')

while True:
    try:
        choice = int(input("""Student Grade manager
    would you like to
    1 add student
    2 update score
    3 view student
    4 view ranked list
    5 delete student
    9 quit
    """))
        if choice == 1:
            add_student()
            continue
        elif choice == 2:
            update_score()
            continue
        elif choice == 3:
            view_student()
            continue
        elif choice == 4:
            view_ranked()
            continue
        elif choice == 5:
            delete_student()
            continue
        elif choice == 9:
            print("bell goes")
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue

logging.disable(logging.CRITICAL)













