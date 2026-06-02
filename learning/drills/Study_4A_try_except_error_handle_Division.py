# Write a program that asks the user for a number, divides 100 by it, and prints the result.
# Use try/except to catch a division by zero error and print "Cannot divide by zero"
# Also catch the case where the user types something that isn't a number.



def user_number():
    try:
        number = int(input('Enter a Number '))
        return 100 / number
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print('you must type in a number')

result = user_number()
print (result)
