
import random, logging, datetime
logging.basicConfig(level=logging.DEBUG)
words = ['python', 'hangman', 'programming', 'function', 'dictionary']
wrong_guesses = 0
max_wrong = 6
guessed = []
hint = False

log = []

def activity_log(action, letter, current_state):
    time = datetime.datetime.now()
    entry = f"{action} {letter} {current_state} guesses left {max_wrong - wrong_guesses}"
    log.append(entry)
    logging.debug(entry)

def hint_help():
    logging.debug("hint help initiated")
    global hint
    hint = True
    hint_options = []
    for i in range(len(display)):
        if display[i] == '_':
            hint_options.append(i)
    if len(hint_options) == 1:
        print("just one letter left you got this!")
        logging.debug("no free solves")
        return
    hint_index = random.choice(hint_options)
    display[hint_index] = secret_word[hint_index]
    print(f"Hint!: {secret_word[hint_index]}")
    print(' '.join(display))
    activity_log("Pity letter", secret_word[hint_index], display)
    return

def verify_guess():
    logging.debug("verify guess initiated")
    global guessed
    guess = input("\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print('invalid input')
        logging.debug(f"invalid input '{guess}' attempted")
        return False
    if guess in guessed:
        print("You already guessed that letter")
        print(f"guessed letters: {guessed}")
        logging.debug("short term memory loss")
        return False
    guessed.append(guess)
    activity_log("User Guessed", guess, wrong_guesses)
    return guess

secret_word = random.choice(words)
display = ['_'] * len(secret_word)
print(f'Word has {len(secret_word)} letters')
print(' '.join(display))
activity_log("God has Chosen", secret_word, display)

while wrong_guesses < max_wrong:
    guess = verify_guess()
    if not guess:
        continue
    if guess in secret_word:
        for i in range(len(display)):
            if secret_word[i] == guess:
                display[i] = secret_word[i]
        print("correct")
        print(' '.join(display))
        activity_log("Correct letter Guessed", guess, display)
        if '_' not in display:
            print('you win')
            break
        continue
    else:
        wrong_guesses += 1
        print(f'wrong! {max_wrong - wrong_guesses} guesses left')
        print(f'guessed so far: {guessed}')
        activity_log("User Guessed Wrong", guess, display)
        if wrong_guesses == 3 and not hint:
            hint_help()
        if wrong_guesses >= max_wrong:
            print(f'you lose, word was {secret_word}')
for item in log:
    print (item)

logging.disable(logging.CRITICAL)























