    Creating List with Repetition
Question: Create a list with 5 underscores using the * operator.

items = ['_'] * 5 → ['_', '_', '_', '_', '_']
Pattern: [value] * number creates a list with that value repeated

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Joining List into String
display = ['p', '_', 't', 'h', '_', 'n']
Question: Join the list into a string with spaces between letters (result: "p _ t h _ n")

Correct: ' '.join(display) → "p _ t h _ n"

Pattern: ' '.join(list) - space separator between items
Pattern: separator.join(list) - the separator string calls .join() on the list

'Common mistake:' thinking its list.join(separator) - its actually the opposite.

''.join(list) → no separator (smooshes together)
' '.join(list) → space separator
', '.join(list) → comma-space separator

The string BEFORE .join() is what goes between items.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Checking String Length
guess = 'ab'
Question: Write an if statement to check if guess is NOT exactly 1 character long.

if len(guess) != 1:
Pattern: len(string) != number checks if length doesnt match

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Checking if String is Alphabetic
guess = '5'
Question: Write an if statement to check if guess is NOT alphabetic.

Correct: if not guess.isalpha():
Pattern: .isalpha() returns True if all characters are letters

Common patterns:
guess.isalpha() - checks if alphabetic
not guess.isalpha() - checks if NOT alphabetic
guess.isdigit() - checks if numeric
guess.isalnum() - checks if alphanumeric

if not guess.isalpha():

Pattern: not string.isalpha() checks if string contains non-letter characters

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Combining Validation Checks
guess = '5'
Question: Write a complete if statement to check if guess is NOT exactly 1 character OR NOT alphabetic. Print "Invalid" if true.

if len(guess) != 1 or not guess.isalpha():
    print('Invalid')
Pattern: if condition1 or condition2: - either condition triggers the block

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Looping Through String by Index
word = 'python'
Question: Write a for loop using range() that prints each index number (0, 1, 2, 3, 4, 5).

for i in range(len(word)):
    print(i)
Result:
0
1
2
3
4
5
Pattern: for i in range(len(sequence)): loops through indices (0 to length-1)
Why this matters: You need the index position to update specific spots in a list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Accessing Character by Index
word = 'python'
i = 2
Question: How would you access the character at position 2 (the 't')?

word[2] → 't'
Pattern: string[index] accesses character at that position

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Comparing Character to Another Character
word = 'python'
guess = 't'
i = 2
Question: Write an if statement to check if the character at position 2 in word equals guess.

if word[i] == guess:
    print('correct')
Pattern: string[index] == value compares character at index to another value

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Modifying List Element by Index
display = ['_', '_', '_', '_', '_', '_']
guess = 't'
i = 2
Question: Replace the underscore at position 2 with the letter 't'.

display[i] = 't'
Result: ['_', '_', 't', '_', '_', '_']
Pattern: list[index] = new_value replaces element at that position

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Letter Reveal Logic
secret_word = 'python'
display = ['_', '_', '_', '_', '_', '_']
guess = 't'
Question: Write a for loop that:

Goes through each index of secret_word
Checks if character at that index equals guess
If yes, updates display at that index with the guess

for i in range(len(secret_word)):
    if secret_word[i] == guess:
        display[i] = guess
        print(display)

Your hangman version (prints AFTER the loop):
for i in range(len(secret_word)):
    if secret_word[i] == guess:
        display[i] = guess
print(' '.join(display))  # Print once after all updates

Both work! Your version prints once after all matches found (cleaner output).
Pattern breakdown:

for i in range(len(string)) - get each index
if string[i] == value - check character at index
list[i] = new_value - update list at same index

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Checking if Value NOT in List
pythondisplay = ['p', '_', 't', 'h', '_', 'n']
Question: Write an if statement to check if there are NO underscores left in display.

if '_' not in display:
Pattern: value not in sequence checks if value doesnt exist, returns True if value doesnt exist in list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Win Condition
display = ['p', 'y', 't', 'h', 'o', 'n']
Question: Write code that checks if there are no underscores left. If true, print "You win!" and break.

if '_' not in display:
    print("You Win!")
    break
Pattern: Check completion condition → feedback → break from loop

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Random Choice from List
import random
words = ['cat', 'dog', 'bird']
Question: Use random to pick one word from the list and assign it to chosen_word.

chosen_word = random.choice(words)
Pattern: random.choice(list) returns a random element from the list
Note: Must import random first

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Putting It All Together
Question: Write a mini hangman game with:

List of 3 words
Pick random word
Create display list with underscores
Print the joined display
Get one guess
Check if guess is in word
If yes, reveal all positions of that letter
Print updated display

(Just one guess, not a full loop)

import random
words = ['cat', 'dog', 'bird']
rand_word = random.choice(words)
display = ['_'] * len(rand_word)
print(' '.join(display))
guess = input("take a guess: ")
for i in range(len(rand_word)):
    if rand_word[i] == guess:
        display[i] = guess
print(' '.join(display))

✓ ['_'] * len(word) - list repetition
✓ ' '.join(list) - joining with spaces
✓ for i in range(len(word)) - index loop
✓ word[i] == guess - character comparison
✓ display[i] = guess - list modification
✓ random.choice(list) - random selection

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Finding Hidden Positions
display = ['p', '_', 't', '_', 'o', 'n']
Question: Write a loop that prints only the indices where theres still an underscore (should print: 1, 3).

for i in range(len(display)):
    if display[i] == '_':
        print(i)
Pattern: Loop through indices → check if underscore → do something with that index

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Collecting Hidden Positions
display = ['p', '_', 't', '_', 'o', 'n']
Question: Create an empty list called hidden_positions, then loop through display and append each index that has an underscore.

hidden_positions = []
for i in range(len(display)):
    if display[i] == '_':
        hidden_positions.append(i)
Result: hidden_positions = [1, 3]
Pattern: Empty list → loop → append matching indices → list of positions

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Random Choice from Collected Positions
import random
hidden_positions = [1, 3, 5]
Question: Pick a random index from hidden_positions and store it in hint_index.

hint_index = random.choice(hidden_positions)
Pattern: Pick random element from list of available positions

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Getting Letter from Secret Word
secret_word = 'python'
hint_index = 3
Question: Get the letter at hint_index from secret_word and store it in hint_letter.

hint_letter = secret_word[hint_index]
If hint_index is 3, hint_letter would be 'h' (from 'python')
Pattern: string[index] gets character at that position

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Revealing Hint in Display
display = ['p', '_', 't', '_', 'o', 'n']
hint_index = 3
hint_letter = 'h'
Question: Update display at hint_index with hint_letter, then print the joined display.

display[hint_index] = hint_letter
print(' '.join(display))
Result: p _ t h o n
Pattern: Update list → print joined result

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    One-Time Hint Trigger
wrong_guesses = 3
hint_given = False
Question: Write an if statement that triggers when wrong_guesses equals 3 AND hint hasnt been given yet.

if wrong_guesses == 3 and not hint_given:
Pattern: Check exact value AND flag not set - ensures one-time execution

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Setting the Flag
Question: Inside that if block, add code to set hint_given = True so it wont trigger again.

if wrong_guesses == 3 and not hint_given:
    hint_given = True

Pattern: Set flag immediately to prevent re-triggering

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 Complete Hint Logic
Question: Combine everything into one block that:

Checks if wrong_guesses == 3 and hint not given
Finds all hidden positions
Picks a random one
Gets that letter from secret_word
Reveals it in display
Prints "Hint!" and the updated display
Sets hint_given = True

pythonimport random
secret_word = 'python'
display = ['p', '_', 't', '_', 'o', 'n']
wrong_guesses = 3
hint_given = False

if wrong_guesses == 3 and not hint_given:
    hint_given = True
    for i in range(len(display)):
        if display[i] == '_':
            hidden_positions.append(i)
    hint_help = random.choice(hidden_positions)
    display[hint_help] = secret_word[hint_help]
    print(f"hint!: {secret_word[hint_help]}")
    print(' '.join(display))
Complete pattern breakdown:

One-time trigger check (exact guess count + flag)
Set flag immediately
Collect all hidden positions
Random selection from available spots
Reveal letter at that position
User feedback

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Where to add this in your hangman loop:
Put it right after wrong_guesses += 1 in your else block:
pythonelse:
    wrong_guesses += 1
    print(f'wrong! {max_wrong - wrong_guesses} guesses left')

    # Hint system here
    if wrong_guesses == 3 and not hint_given:
        hint_given = True
        # ... rest of your hint code
Dont forget: Initialize hint_given = False at the top with your other variables.







































































































