# Write a function called sum_list that takes a list of numbers
# loops through them, adds them all together and returns the total. Print the result.
# Test it with:
# numbers = [3, 7, 2, 9, 4, 1, 4]

numbers = [3, 7, 2, 9, 4, 1, 4]
def sum_list(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

total = sum_list(numbers)
print(total)
