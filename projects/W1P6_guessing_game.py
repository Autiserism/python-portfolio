'''
Random number 1-100.
Give the user unlimited guesses.
Track how many guesses it took.
After winning ask if they want to play again.
'''



import random
def guessing_game():
    secret_number = random.randint(1, 100)
    guesses_taken = 0
    print('Guess a number between 1 and 100.')
    print('You have unlimited guesses')
    while True:
        guesses_taken = guesses_taken + 1
        try:
            guess = int(input('Take a Guess: '))
        except ValueError:
            print("Invalid input")
            continue
        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break
    print(f'Correct you got it in {guesses_taken} guesses')
while input("Play again? yes or no: ") == 'yes':
    guessing_game()
print('play guesing game?')
if input("yes or no: ") == ('yes'):
    guessing_game()
else:
    print('ok')

