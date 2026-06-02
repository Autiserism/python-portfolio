'''
Store a list of words. Pick one randomly.
Display blanks for each letter.
Ask the user to guess one letter at a time.
Track wrong guesses. Win when all letters are found,
lose after 6 wrong guesses.
'''

import random  # Import Python's random module so we can randomly pick a word.

words = ['python', 'hangman', 'programming', 'function', 'dictionary']  # Create a list of possible secret words.

wrong_guesses = 0  # Start the wrong guess counter at 0.

max_wrong = 6  # Set the maximum number of wrong guesses allowed before losing.

guessed = []  # Create an empty list to store letters the player has already guessed.

secret_word = random.choice(words)  # Pick one random word from the words list and save it as the secret word.

display = ['_'] * len(secret_word)  # Create a list of underscores, one underscore for each letter in the secret word.

print(f'Word has {len(secret_word)} letters')  # Tell the player how many letters are in the secret word.

print(' '.join(display))  # Show the hidden word as spaced-out underscores, like "_ _ _ _ _".

while wrong_guesses < max_wrong:  # Keep looping as long as the player has not reached the max wrong guesses.

    guess = input('guess a letter: ').lower()  # Ask the player for a letter and convert it to lowercase.

    if len(guess) != 1 or not guess.isalpha():  # Check if the input is not exactly one alphabet letter.
        print("invalid input")  # Tell the player their input was not valid.
        continue  # Skip the rest of this loop and ask for another guess.

    if guess in guessed:  # Check if the player already guessed this letter before.
        print("already guessed")  # Tell the player they already used that letter.
        continue  # Skip the rest of this loop and ask again.

    guessed.append(guess)  # Add the valid new guess to the guessed list.

    if guess in secret_word:  # Check if the guessed letter appears anywhere in the secret word.

        for i in range(len(secret_word)):  # Loop through every index position in the secret word.

            if secret_word[i] == guess:  # Check if the letter at this position matches the guessed letter.
                display[i] = guess  # Reveal that guessed letter in the same position in the display list.

        print(' '.join(display))  # Print the updated display with revealed letters and remaining underscores.

        if '_' not in display:  # Check if there are no underscores left, meaning the whole word is guessed.
            print('you win')  # Tell the player they won.
            break  # Exit the while loop because the game is over.

    else:  # Run this block if the guessed letter is not in the secret word.

        wrong_guesses += 1  # Add 1 to the wrong guess counter.

        print(f'wrong! {max_wrong - wrong_guesses} guesses left')  # Show how many wrong guesses remain.

        print(f'guessed so far: {guessed}')  # Show all letters guessed so far.

        if wrong_guesses >= max_wrong:  # Check if the player has reached the losing limit.
            print(f'you lose, word was {secret_word}')  # Tell the player they lost and reveal the word
'''

import random

words = ['python', 'hangman', 'programming', 'function', 'dictionary']
wrong_guesses = 0
max_wrong = 6
guessed = []

secret_word = random.choice(words)
display = ['_'] * len(secret_word)
print(f'Word has {len(secret_word)} letters')
print(' '.join(display))

while wrong_guesses < max_wrong:
    guess = input('guess a letter: ').lower()
    if len(guess) != 1 or not guess.isalpha():
        print("invalid input")
        continue
    if guess in guessed:
        print("already guessed")
        continue
    guessed.append(guess)
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
        print(' '.join(display))
        if '_' not in display:
            print('you win')
            break
    else:
        wrong_guesses += 1
        print(f'wrong! {max_wrong - wrong_guesses} guesses left')
        print(f'guessed so far: {guessed}')
        if wrong_guesses >= max_wrong:
            print(f'you lose, word was {secret_word}')
'''




