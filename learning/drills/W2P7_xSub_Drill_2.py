'''
List comprehension in functions
Write a function called analyze that takes a list of numbers
and returns a dictionary with four keys — evens, odds, above_50 and below_50 —
each containing a list built with list comprehension.
'''

numbers = [11, 82, 17, 67, 45, 65, 84, 20, 4, 30, 49, 19, 26, 90, 26, 95, 53, 6, 10, 47]
num_stats = {}
def analyze():
    num_stats['even'] = even = [num for num in numbers if num % 2 == 0]
    num_stats['odd'] = odd = [num for num in numbers if num % 2 != 0]
    num_stats['above 50'] = above_50 = [num for num in numbers if num >= 50]
    num_stats['below 50'] = below_50 = [num for num in numbers if num < 50]
analyze()
print(num_stats)


















