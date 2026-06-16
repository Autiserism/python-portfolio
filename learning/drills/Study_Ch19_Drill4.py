'''
Drill 4 — Final Chapter 19 drill
Write a program that:

Asks the user for two dates in MM/DD/YYYY format
Calculates how many days are between them
Prints which date is earlier
Prints what day of the week each date falls on

Use strptime() and timedelta.
'''
import re,datetime,time,random
def numdum(n):
    if n < 10:
        n = '0' + str(n)
    return n
pattern = re.compile(r"([0][0-9]|1[0-2])\/([0-2][0-9]|[3][0-1])\/(\d{4})")
def ask_date():
    m = random.randint(1,12)
    m = numdum(m)
    d = random.randint(1,31)
    d = numdum(d)
    y = random.randint(1970,2026)
    while True:
        user_date = f'{m}/{d}/{y}'#input(f'enter a date in MM/DD/YYYY format\n')
        match = pattern.search(user_date)
        if not match:
            print(f'requires exact format ex. {m}/{d}/{y}')
            continue
        break
    return user_date
date1 = ask_date()
date2 = ask_date()
date1 = datetime.datetime.strptime(date1, '%m/%d/%Y')
date2 = datetime.datetime.strptime(date2, '%m/%d/%Y')
print(date1)
print(date2)
if date1 < date2:
    print(f"the first date entered comes before the second")
    days_between = datetime.datetime(date2.year,date2.month,date2.day) - datetime.datetime(date1.year,date1.month,date1.day)
if date1 > date2:
    print(f"the second date entered comes before the first")
    days_between = datetime.datetime(date1.year,date1.month,date1.day) - datetime.datetime(date2.year,date2.month,date2.day)
if date1 == date2:
    print('its the same day')
    days_between = datetime.timedelta(0)
print(f"there are {days_between.days} days between the two dates")
print(f"the first date was on a {date1.strftime('%A')}")
print(f"the second date was on a {date2.strftime('%A')}")







