# CH3 - Loops
# Input -> loop -> condition -> output

import sys

secret = 7
attempts = 0
max_attempts = 3

print("Guess the number between 1 and 10.")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")

    if attempts >= max_attempts:
        print(f"Out of attempts. The number was {secret}.")
        sys.exit()
'''
Plain English logic walk through:

1 Set the secret number, attempt counter and max attempts
2 Loop forever until the player guesses correctly or runs out of attempts
3 Each pass increment the attempt counter
4 Check if correct — break out of loop
5 If not correct give a hint
6 After the hint check if attempts are used up — exit the program if so
'''

Examples

"1. While Loop"
while _______:
    _______


count = 0
while count < 5:
    print(count)
    count = count + 1
'''
Plain English:
Keep running the block of code as long as the condition stays True.
Always make sure something inside the loop eventually makes the condition False or it runs forever.

Use cases:
Repeating until a condition is met
Keeping a program running until the user quits
Game loops
'''


"2. While True Loop"
while True:
    _______
    if _______:
        break


while True:
    name = input("Enter your name: ")
    if name != "":
        break
print(f"Hello {name}")
'''
Plain English:
Loop forever until a break condition is met.
Useful when you don't know in advance how many times to loop — you just know when to stop.

Use cases:
Input validation — keep asking until valid input is received
Menus — keep showing until user chooses to quit
Guessing games
'''


"3. For Loop with Range"
for _______ in range(_______):
    _______


# Count from 0 to 4
for i in range(5):
    print(i)

# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Count from 0 to 20 by 2
for i in range(0, 21, 2):
    print(i)
'''
Plain English:
Repeat a block a set number of times. range(n) counts from 0 to n-1.
range(a, b) counts from a to b-1. range(a, b, step) counts from a to b-1 jumping by step each time.

Use cases:
Repeating something a known number of times
Counting up or down
Generating sequences of numbers
'''


"4. For Loop Through a List"
for _______ in _______:
    _______


fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
'''
Plain English:
Go through every item in a list one at a time. The loop variable holds each item for that pass.
Singular variable name for the item, plural for the list.

Use cases:
Processing every item in a list
Searching through a list
Building a new list from an existing one
'''


"5. Break and Continue"
# break - exit loop entirely
for _______ in _______:
    if _______:
        break

# continue - skip this pass, keep looping
for _______ in _______:
    if _______:
        continue
    _______



# Stop when hitting 5
for i in range(10):
    if i == 5:
        break
    print(i)

# Skip multiples of 3
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
'''
Plain English:
break — immediately exits the loop, nothing below it in the loop runs
continue — skips the rest of this pass and jumps back to the top of the loop

Use cases:
break — stopping a search when you find what you need
continue — skipping invalid or unwanted values
'''


"6. Nested Loops"
for _______ in _______:
    for _______ in _______:
        _______

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
'''
Plain English:
A loop inside a loop. The inner loop runs completely for every single pass of the outer loop.

Use cases:
Processing lists within lists
Building multiplication tables
Comparing every item in one list against every item in another
'''


"7. sys.exit()"
import sys
if _______:
    sys.exit()

import sys
answer = input("Continue? y/n: ")
if answer == "n":
    sys.exit()
print("Program continues")
'''
Plain English:
Immediately kills the entire program. Nothing after it runs. Requires import sys at the top.

Use cases:
Exiting a program based on user choice
Stopping a program when a critical error occurs
'''
