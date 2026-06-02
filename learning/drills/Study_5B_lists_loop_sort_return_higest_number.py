# Write a function called find_max that takes a list of numbers,
# loops through it and returns the largest number
# WITHOUT using the built in max() function.
# Test it with: numbers = [3, 17, 2, 45, 8, 23, 11]


# numbers = [3, 17, 2, 45, 8, 23, 11]
#def find_maxx (numbers):   this changes the original list works but is often not the right option
#    numbers.sort()
#    return numbers[-1]

#max_numm = find_maxx(numbers)
#print(max_numm)

numbers = [3, 17, 2, 45, 8, 23, 11]
def find_max(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
max_num = find_max(numbers)
print(max_num)
# the looping way keeps the original list the same
