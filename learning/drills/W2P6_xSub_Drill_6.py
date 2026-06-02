'''
Full pattern combined
Write a word guessing game where the secret word is picked from a list of 10 words.
Display progress as _ _ _ _ _. Track guesses. Win when complete.
Lose after 5 wrong.
But this time add a hint system — after 3 wrong guesses reveal the first letter automatically.
'''

import random

words = ['Red', 'Green', 'Blue', 'Purple', 'Cyan', 'Dog', 'Moose', 'Cow', 'AntEater', 'Dragon']
worde = random.choice(words).lower()
display = ['_'] * len(worde)
guesses = 0
guessed_letters = []
lose_condition = 5
print(worde)

print("guess the word you have 5 attempts")
while guesses < lose_condition:
    if guesses = 3:
        hint = worde[0]
        display[0] = hint
    if '_' not in display:
        print('you win')
        break
    print(' '.join(display))
    guess = input("enter a guess: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("invalid input")
        continue
    if guess in guessed_letters:
        print(f"letter already guessed {guessed_letters}")
        continue

    if guess in worde:
        for i in range(len(worde)):
            if worde[i] == guess:
                guessed_letters.append(guess)
                display[i] = guess
                continue
    else:
        print('wrong guess')
        guessed_letters.append(guess)
        print(f'guessed letters \n{guessed_letters}')
        guesses += 1
    if guesses == 5:
        print (f'you lose the word was {worde}')






















