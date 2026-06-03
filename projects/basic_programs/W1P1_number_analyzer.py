'''
Ask the user for 5 numbers one at a time,
store them in a list,
then print the highest, lowest, sum and average.
Use functions for each calculation.
'''



numbers = []

for i in range(0,5):
    numbers.append(int(input('enter a number ')))
print(numbers)

def num_H(numbers):
        return max(numbers)

def num_L(numbers):
        return min(numbers)

def num_sum(numbers):
        return sum(numbers)

def num_av(numbers):
    return sum(numbers) / len(numbers)


Hinum = num_H(numbers)
print(f'{Hinum} Higest number')

Lonum = num_L(numbers)
print(f'{Lonum} Lowest number')

total = num_sum(numbers)
print(f'{total} Sum of numbers')

average = num_av(numbers)
print(f'{average} is the average')








