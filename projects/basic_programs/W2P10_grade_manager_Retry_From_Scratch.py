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
def get_grade(ave):
    if ave >= 90:
        return 'A'
    elif ave >= 75:
        return 'B'
    elif ave >= 60:
        return 'C'
    else:
        return 'F'

def find_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None

def get_average(student_grades):
    return int(sum(student_grades.values()) / len(student_grades))

def add_student():
    name = input('name = ')
    check = find_student(name)
    if not check:
        print('already exists')
        return
    student_grades = {'math' : 00, 'english' : 00, 'gym' : 00}
    for k in student_grades:
        mark = int(input(f'Enter {k} Score: '))
        student_grades[k] = mark
    ave = get_average(student_grades)
    grade = get_grade(ave)
    print(f"{name} Added \nCurrent grade {grade}")
    students.append({'name': name, 'average': ave, 'subjects' : student_grades})
    logging.debug(f'{name} Added to students')

def update_score():
    name = input('enter name: ').title()
    student = find_student(name)
    if not student:
        print(f"{name} isnt in the students list")
        return
    print(student['name'])
    for i, s in student['subjects'].items():
        print(i, s)
    choice = input('enter subject to update: ').lower
    if choice not in student['subjects']:
        print('invalid input')
        return
    new_score = int(input(f"enter new score for {choice}: "))
    student['subjects'][choice] = new_score
    student['average'] = get_average(student['subjects'])
    print(f"{name}'s {choice} score updated to {new_score}")
    print(f"updated average = {student['average']} \nGrade = {get_grade(student['average'])}")
    logging.debug(f"{name}, {choice} score changed to {new_score}")

def view_student():
    name = input('enter name: ').title()
    student = find_student(name)
    if not student:
        print(f"{name} not found")
        return
    print(student['name'])
    print(f"Average = {student['average']} \nGrade = {get_grade(student['average'])} ")
    for i, s in student['subjects'].items():
        print(i,s)
    return

def view_ranked():
    ranked = sorted(students, key=lambda x:x['average'], reverse=True)
    for i,student in enumerate(ranked, 1):
        print (f"{i}, {student['name']} {student['average']} {get_grade(student['average'])}")

def delete_student():
    name = input('enter name: ').title()
    student = find_student(name)
    if not student:
        print(f"{name} not found")
        return
    if input('are you sure yes/no: ') != 'yes':
        return
    students.remove(student)
    print(f'{name} has been expelled')
    logging.debug(f"{name} removed ")

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
