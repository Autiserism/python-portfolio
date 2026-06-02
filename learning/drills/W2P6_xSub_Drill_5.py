'''
random.choice() vs random.randint()
Write a program that has three lists — colors, animals and adjectives.
Use random.choice() to pick one from each and combine them into a random character name.
Generate 5 names and print them.
'''

import random
colors = ['Red', 'Green', 'Blue', 'Purple', 'Cyan']
animals = ['Dog', 'Moose', 'Cow', 'Ant-Eater', 'Dragon']
adjectives = ['tasteless', 'square', 'desperate', 'vengeful', 'hot']
for i in range(0, 5):
    c = random.choice(colors)
    A = random.choice(animals)
    a = random.choice(adjectives)
    print(a, c, A)

























