'''
Drill 3
Write a program that:

Uses time.sleep() to build a countdown timer
Ask the user how many seconds to count down from
Print each second remaining
Print "Time's up!" when done
'''

import time,datetime
while True:
    try:
        amount = int(input("how many seconds to countdown from: "))
        break
    except ValueError:
        print ("numbers are hard")
        continue
print('Time start')
for i in range(amount, 0, -1):  # counts down from amount to 1
    print(i)
    time.sleep(1)

print("Time's up!")




















