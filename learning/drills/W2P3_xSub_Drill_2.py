'''
Multiple return values

Write a function called list_stats that takes a list of numbers and returns
minimum, maximum, average and total as four separate values.
Unpack and print them all.
'''

def list_stats (lon):
    minimum = min(lon)
    maximum = max(lon)
    average = sum(lon) / len(lon)
    total = sum(lon)
    return minimum, maximum, average, total

lon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mini, maxi, ave, tot = list_stats(lon)
print(list_stats(lon))  # prints raw tuple (1, 10, 5.5, 55)

# cleaner:
print(f'Minimum: {mini}')
print(f'Maximum: {maxi}')
print(f'Average: {ave}')
print(f'Total: {tot}')


















