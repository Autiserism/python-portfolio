import random

questions = [
    {'question': 'tq1', 'answer': 't'},
    {'question': 'fq1', 'answer': 'f'},
    {'question': 'tq2', 'answer': 't'},
    {'question': 'fq2', 'answer': 'f'},
    {'question': 'tq3', 'answer': 't'},
]

random.shuffle(questions)

total_correct = 0

print(f"you will be asked 5 true or false questions \nAnswer with 't' or 'f' ")
for item in questions:
    print(item['question'])
    user_answer = input('t or f: ')
    if user_answer not in ['t','f']:
        print ('invalid answer')
        continue
    if user_answer == item['answer']:
        print('correct')
        total_correct +=1
    else:
        print(f"incorrect, answer was {item['answer']}")
print(f'you got {total_correct} right')



'''
Drill 3
Write a program that asks 5 True/False questions stored as dictionaries.
Accept 't' or 'f' as input. Reject anything else.
Track score and show final result.




import random



tfq = {'true' : ['tq1', 'tq2', 'tq3', 'tq4', 'tq5'],
'false' : ['fq1', 'fq2', 'fq3', 'fq4', 'fq5']
}

questions_asked = 0
total_correct = 0

alt_index = 0

print(f"you will be asked 5 true or false questions \nAnswer with 't' or 'f' ")

while questions_asked < 5:
    PickANum = random.randint(0, 100)
    if PickANum >= 50:
        correct_answer = 't'
        torf = 'true'
    else:
        correct_answer = 'f'
        torf = 'false'
    print(tfq[torf][alt_index])
    if user_answer not in ['t', 'f']:
        print('enter t or f only')
        continue

    if user_answer == correct_answer:
        print(f'{correct_answer} was the correct answer')
        total_correct += 1
    else:
        print(f'incorect the right answer was {correct_answer}')
    questions_asked += 1
    alt_index += 1

print(f'you got {total_correct} right')
'''











