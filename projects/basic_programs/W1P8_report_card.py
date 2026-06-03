'''
Ask for a student name and 5 subject scores.
Store in a dictionary.
Calculate the average.
Print a formatted report card using f-strings and string padding.
'''

# define get_average(scores)
#     total = 0
#     for score in scores.values()
#         total = total + score
#     return total / len(scores)

# define get_grade(average)
#     if average >= 90 return 'A'
#     elif average >= 80 return 'B'
#     elif average >= 70 return 'C'
#     elif average >= 60 return 'D'
#     else return 'F'

# define print_report(student)
#     print header with student name centered
#     for subject, score in student scores items
#         print subject ljust padded and score
#     print divider line
#     print average and grade

# ask for student name
# ask for number of subjects
# loop through subjects
#     ask for subject name
#     ask for score
#     add to scores dictionary
# build student dictionary
# call print_report



def get_average(scores):
    total = 0
    for score in scores.values():
        total = total + score
    return total / len(scores)

def get_grade (average):
    if average >= 90:
        return ('A')
    elif average >= 80:
        return ('B')
    elif average >= 70:
        return ('C')
    elif average >= 60:
        return ('D')
    else:
        return ('F')

def print_report(student):
    print(f"{student['name']}".center(11, '*'))
    for subject, score in student['scores'].items():
        print(f'{subject}'.ljust(9,'-') + f'{score}')

    print('v'.center(11,'='))
    average = get_average(student['scores'])
    grade = get_grade(average)
    print(f'Average: {average:.1f}')
    print(f'Grade: {grade}')


student = {'name': '', 'scores': {}}
name = input('whats your name: ')
student['name'] = name
num_of_sub = int(input('how many subjects?: '))
for i in range(num_of_sub):
    sub_name = input('Enter the subjects name: ' )
    sub_score = int(input('what was the score?: '))
    student['scores'][sub_name] = sub_score

print_report(student)

# scores keys are subject names, values are scores
# example: {'name': 'Tyler', 'scores': {'Math': 92, 'English': 88}}








