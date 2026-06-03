'''
W2P9 — Word Scrambler
Ask for a word. Scramble the letters randomly.
Show the scrambled word and ask the user to guess the original.
Give 3 attempts. Use string and list methods.
'''
import random
word_list = ['Purple', 'Moose', 'AntEater', 'Dragon', 'tasteless', 'square', 'desperate', 'vengeful']
def scramble_word(word):
    word = word.lower()
    letters = list(word)
    while True:
        random.shuffle(letters)
        scrambled = ''.join(letters)
        if scrambled != word:
            break
    return scrambled
def play_game():
    selected_word = random.choice(word_list).lower()
    scrambled = scramble_word(selected_word)
    attempts = 0
    max_attempts = 3
    print(f'unscramble this word: {scrambled}')
    print(f'you have {max_attempts} attempts')
    while attempts < max_attempts:
        guess = input('your guess: ').lower().strip()
        if guess == selected_word:
            print ('correct')
            return True
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f'wrong, {remaining} attempts left')
        else:
            print(f'out of attempts, the word was {selected_word}')
            return False
wins = 0
losses = 0
while True:
    if play_game():
        wins += 1
    else:
        losses += 1
    print(f'Score: {wins} wins, {losses} losses')
    if input('play again? yes/no: ').lower() != 'yes':
        break
