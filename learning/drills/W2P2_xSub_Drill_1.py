'''
Drill 1
Write a program that loops through a list of dictionaries with keys 'word' and 'definition'.
Print each word, ask the user to type the definition, check if correct.
Track score and show percentage at end.
'''

wordinary = [
{'word' : 'gort' ,'definition' : 'gleebe' },
{'word' : 'glimb' ,'definition' : 'wimba' },
{'word' : 'tort' ,'definition' : 'zatsa' },
{'word' : 'delwep' ,'definition' : 'AAAAAAh' }
]

toatwords = 0
num_correct = 0
while toatwords < len(wordinary):
    print(f'write word definitions {toatwords+1} out of {len(wordinary)}')
    print(wordinary[toatwords]['word'])
    correct_answer = wordinary[toatwords]['definition'].lower()
    user_answer = input('whats the words definition: ').strip().lower()
    if correct_answer == user_answer:
        print('correct')
        num_correct += 1
        toatwords += 1
        continue
    else:
        print(f'incorect the correct definition was {correct_answer}')
    toatwords +=1
percentage = (num_correct / len(wordinary)) * 100
print(f' you got {num_correct} \nthats {percentage}%')
if percentage >= 80:
    print('ver goode')
elif percentage >= 60:
    print('gud')
else:
    print('no gid')




















