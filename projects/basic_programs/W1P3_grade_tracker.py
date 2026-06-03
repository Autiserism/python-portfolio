'''
Ask the user to enter student names and scores until they type done.
Store in a list of dictionaries.
Print a sorted report showing each student, their score and their letter grade.
'''


names_score = []

while True:
    name = input("Enter a name or nothing to finish: ")
    if name == '':
        break
    score = int(input("Enter score: "))
    names_score.append({'name': name, 'score': score})


def score_sort(names_score):
    grade = {'A':[], 'B':[], 'C':[], 'F':[]}
    for people in names_score:
        name = people['name']
        score = people['score']
        if score >= 90:
            grade['A'].append(name)
        elif score >=70:
            grade['B'].append(name)
        elif score >=50:
            grade['C'].append(name)
        else:
            grade['F'].append(name)
    return grade


result = score_sort(names_score)
print(result)























