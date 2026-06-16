'''
Drill 2
Write a program that:

Asks the user for their birthdate in MM/DD/YYYY format
Calculates their exact age in years
Calculates how many days until their next birthday
Prints what day of the week they were born on

Use strptime() to convert the input and timedelta for the math.
Go.
'''

import re,datetime,time,random

def numdum(n):
    if n < 10:
        n = '0' + str(n)
    return n

m = random.randint(1,12)
m = numdum(m)
d = random.randint(1,31)
d = numdum(d)
y = random.randint(1970,2026)

pattern = re.compile(r"([0][0-9]|1[0-2])\/([0-2][0-9]|[3][0-1])\/(\d{4})")

while True:
    user_bday = f'{m}/{d}/{y}'#input(f'enter birthdate in MM/DD/YYYY format\n')'08/04/1972'
    match = pattern.search(user_bday)
    if not match:
        print(f'requires exact format ex. {m}/{d}/{y}')
        continue
    break
#month = int(match.group(1))
#day = int(match.group(2))
#year = int(match.group(3))
#dt = datetime.datetime(year,month,day)

dt = datetime.datetime.strptime(user_bday, '%m/%d/%Y')
#print(dt)
gap = datetime.datetime.now() - datetime.datetime(dt.year,dt.month,dt.day)
age_calc = gap.days / 365
print(f"you are {round(age_calc)} years old")
now = datetime.datetime.now()


# next birthday this year
next_bday = datetime.datetime(now.year, dt.month, dt.day)

# if already passed this year, use next year
if next_bday < now:
    next_bday = datetime.datetime(now.year + 1, dt.month, dt.day)

days_until = (next_bday - now).days
print(f"your next birthday is in {days_until} days")
print(dt.strftime('you were born on a %A'))

'''
days_past =(datetime.datetime.now() - datetime.datetime(now.year,dt.month,dt.day))
#print(days_past.days)

if days_past.days < 0:
    print(f"your next birthday is in {days_past.days * -1} days")

if days_past.days >= 0:
    next_bday = 365 - days_past.days            #365 - datetime.timedelta(days=days_past.days)
    print(f"your next birthday is in {next_bday} days")




#print(now.year, now.month, now.day)
#print(now.hour, now.minute, now.second)
yer = now.year - dt.year
mon = now.month - dt.month
day = now.day - dt.day

'''






