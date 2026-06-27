'''
Drill 2
Write a program that:

Reads a CSV file of student scores
Calculates the average score for each student
Writes a new CSV file with the results — name and average columns
Prints a summary to the terminal

Create the input CSV manually or generate it in code first.
'''

import csv , os,random
from pathlib import Path
data_path = Path.home() / 'projects' / 'CH18ATBS'
data_path.mkdir(parents=True,exist_ok=True)
os.chdir(data_path)

def random_score():
    return random.randint(1,100)

def random_name():
    name = []
    for i in range(7):
        e = random.randint(97,122)
        name.append(chr(e))
    return (''.join(name))

def add_student():
    _ = {'name':'','scores':{}}
    _['name'] = random_name()
    _['scores']['math'] = random_score()
    _['scores']['english']= random_score()
    _['scores']['gym'] = random_score()
    average = get_average(_['scores'])
    _['average'] = round(average)
    return _

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

with open('ATBSCh18D2.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name','scores', 'subjects','average'])#
    writer.writeheader()
    for i in range(4):
        writer.writerow(add_student())

print(f"{'*'*10}students and scores{'*'*10}")
with open('ATBSCh18D2.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print('Name',row['name'],'Average'.ljust(9,'='),row['average'])  # row['scores'], row['subjects'],



