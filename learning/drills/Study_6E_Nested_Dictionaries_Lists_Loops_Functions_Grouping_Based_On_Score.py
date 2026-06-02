# Write a function called group_by_grade that takes a list of student dictionaries
# and groups them by letter grade into a new dictionary.
# Each grade letter is a key and the value is a list of student names with that grade.
# Expected output: {'A': ['Tyler', 'Jess'], 'B': ['Sarah', 'Anna'], 'F': ['Bob', 'Mike']}
# Scale: 90+ = A, 70+ = B, below 70 = F

students = [
    {'name': 'Tyler', 'score': 92},
    {'name': 'Bob', 'score': 65},
    {'name': 'Sarah', 'score': 88},
    {'name': 'Mike', 'score': 45},
    {'name': 'Jess', 'score': 92},
    {'name': 'Anna', 'score': 73}]


def group_by_grade(students):
    grades = {'A': [], 'B': [], 'F': []}
    for student in students:
        name = student['name']
        score = student['score']
        if score >= 90:
            grades['A'].append(name)
        elif score >= 70:
            grades ['B'].append(name)
        else:
            grades ['F'].append(name)
    return grades


result = group_by_grade(students)
print(result)

