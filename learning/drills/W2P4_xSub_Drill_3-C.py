'''
Drill C — Inline if (ternary)
Write a function called classify that takes a number and returns:

'high' if above 75
'medium' if above 40
'low' if 40 or below

Use the inline if pattern. Test with 6 different numbers.
'''

def classify(numbre):
    soup = 'lies' if numbre > 140 else 'high' if numbre >= 110 else 'medium' if numbre >= 90 else 'low'
    return soup

chances = 6

while chances != 0 :

    try:
        numbre = int(input('enter IQ: '))
    except ValueError:
        print ('off the charts')
        chances -= 1
        print(f"you've got {chances} attempts left ")
        continue
    print ('standby for advaced super computer calculation')
    print('beeb boop')
    print('it has been evaluated')
    print(f'the round table has deemed the {numbre} to be {classify(numbre)}')
    chances -= 1
    print(f'you have {chances} chances left make it into the club make them count or else')
    continue

print('if you got this far You are now manually breathing')



















