# Write a function called count_positives that takes a list of numbers,
# loops through it, counts how many are positive (greater than 0)
# and returns that count. Print the result.
# Test it with: numbers = [4, -2, 0, 7, -5, 3, -1, 9]

numbers = [4, -2, 0, 7, -5, 3, -1, 9]

def count_positives(numbers):
    count = 0
    for greater in numbers:
        if greater > 0:
            count = count + 1
    return count
result = count_positives(numbers)
print(result)
