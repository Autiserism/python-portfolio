'''
Drill 2
Write a program that stores a list of math questions as dictionaries with keys 'question' and 'answer'.
Loop through, ask each, check answer, show score.
Use int() conversion and handle invalid input with try/except.
'''


maths_questions = [
{'question' : 'whats 4 + 3 ' , 'answer': 7},
{'question' : 'whats 9 * 3 ' , 'answer': 27},
{'question' : 'whats 7 / 7 ' , 'answer': 1},
{'question' : 'whats 8 - 3 ' , 'answer': 5},
]

maths_index = 0

total_correct = 0

while maths_index < len(maths_questions):
    print(f'{maths_index+1} question out of {len(maths_questions)}')
    print(maths_questions[maths_index]['question'])
    correct_answer = maths_questions[maths_index]['answer']
    try:
        user_answer = int(input('> '))
    except ValueError:
        print('invalid answer try again')
        continue
    if user_answer == correct_answer:
        print (f"{correct_answer} was right {len(maths_questions) - maths_index-1} questions to go")
        total_correct +=1
        maths_index +=1
        continue
    else:
        print(f'incorect answer the correct answer was {correct_answer}')
        maths_index +=1

#elif user_answer == '':
 #















