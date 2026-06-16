'''
Drill 1
Write a program that:

Prints the current date and time in a readable format using strftime()
Prints how many seconds have passed since the Unix epoch using time.time()
Prints the current day of the week
'''

import datetime,time

dt = datetime.datetime.now()
print(dt.strftime('%A, %B %d %Y, %I:%M %p'))

print(time.time())

print('it is', dt.strftime('%A'))




















