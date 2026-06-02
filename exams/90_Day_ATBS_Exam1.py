'''
Section 1: Core Python (Ch 1-4)
Test: Open blank file, build this in 20 minutes with no notes:
Build a number analyzer:
- Ask user for 5 numbers
- Print: highest, lowest, average
- Tell them how many are above average
- Use functions for each calculation
Pass: Built it, works, took under 20 min
Fail: Needed notes or help for basic structure
'''
Passed


def number_ask():
    numbers = []
    for i in range(5):
        num = int(input(f'({i+1}/5) enter a number: '))
        numbers.append(num)
    return numbers

def highest(numbers):
    most = max(numbers)
    return most

def lowest(numbers):
    least = min(numbers)
    return least

def average(numbers):
    ave = sum(numbers) / len(numbers)
    return ave

def above_average(numbers, ave):
    abv = []
    for num in numbers:
        if num > ave:
            abv.append(num)
    return len(abv)

num = number_ask()
largest = highest(num)
smallest = lowest(num)
ave = average(num)
amoabv = above_average(num, ave)

print (f'''
out of 5 numbers asked
The largest was {largest},
The smallest {smallest},
The average {ave}
and how many of thoes numbers were above average {amoabv}
''')











































