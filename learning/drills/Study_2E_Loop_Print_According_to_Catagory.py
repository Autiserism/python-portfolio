# Write a program that loops through this list of numbers and prints:
#"positive" if the number is greater than 0
#"negative" if the number is less than 0
#"zero" if the number equals 0
# numbers = [4, -2, 0, 7, -5, 0, 3]

numbers = [4, -2, 0, 7, -5, 0, 3]

for number in numbers:
    if number == 0:
        print('Zero')
    elif number > 0:
        print('Positive')
    elif number < 0:
        print('Negative')
