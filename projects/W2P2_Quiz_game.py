'''
Store 10 questions and answers in a list of dictionaries.
Ask each question, check the answer,
track the score.
Display final results with percentage.
Use try/except for invalid input.
'''

qna = [
{'Question':'q1','Answer':'a1'},
{'Question':'q2','Answer':'a2'},
{'Question':'q3','Answer':'a3'},
{'Question':'q4','Answer':'a4'},
{'Question':'q5','Answer':'a5'},
{'Question':'q6','Answer':'a6'},
{'Question':'q7','Answer':'a7'},
{'Question':'q8','Answer':'a8'},
{'Question':'q9','Answer':'a9'},
{'Question':'q10','Answer':'a10'},]

q_index = 0
total_correct = 0

while q_index < len(qna):
    print(f'Question {q_index+1} out of {len(qna)}')
    print(qna[q_index]['Question'])
    correct_answer = qna[q_index]['Answer'].lower()
    user_answer = input('> ').strip().lower()
    if user_answer == '':
        print('invalid answer')
        continue
    if user_answer == correct_answer:
        print ('correct')
        total_correct += 1
        q_index += 1
        continue
    else:
        print (f'incorrect,\nThe correct answer is: {correct_answer}')
    q_index += 1
percentage = (total_correct / len(qna)) * 100
if percentage == 100:
    print('Perfect score!')
elif percentage >= 70:
    print('Good work!')
else:
    print('Keep practicing!')
print(f'{total_correct} out of {len(qna)}\nThats {percentage}% ')


# qna = list of 10 dictionaries
#     each has 'question' and 'answer' keys
#     fill with real questions

# total_correct = 0
# q_index = 0

# while q_index < len(qna)
#     print question number out of total
#     print question
#     user_answer = input.strip().lower()
#     if user_answer == '' print invalid, continue
#     correct = qna[q_index]['answer'].lower()
#     if user_answer == correct
#         print correct
#         total_correct += 1
#     else
#         print incorrect, show correct answer
#     q_index += 1

# percentage = (total_correct / len(qna)) * 100
# print final score and percentage

