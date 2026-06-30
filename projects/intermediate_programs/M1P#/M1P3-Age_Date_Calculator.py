'''
M1P3 — Age / Date Calculator (Ch 19)
Enter a birthdate, get back age in years/months/days, days until next birthday, and the day of the week you were born.
Bonus: calculate days between any two dates. Input validation for date formatting.
'''
import time,datetime,re,random
now = datetime.datetime.now()
pattern = re.compile(r"([0][0-9]|1[0-2])\/([0-2][0-9]|[3][0-1])\/(\d{4})")
def numdum(n):
    if n < 10:
        n = '0' + str(n)
    return n
def vali_date():
    m = random.randint(1,12)
    m = numdum(m)
    d = random.randint(1,28)
    d = numdum(d)
    y = random.randint(1970,2026)
    while True:
        user_date = input(f'enter the date in MM/DD/YYYY format\n')#f'{m}/{d}/{y}'#
        match = pattern.search(user_date)
        if not match:
            print(f'requires exact format ex. {m}/{d}/{y}')
            continue
        break
    return user_date

def bday_stats():
    print('For your Birthday')
    user_bday = vali_date()
    print(user_bday)
    user_bday = datetime.datetime.strptime(user_bday, '%m/%d/%Y')
    gap = now - datetime.datetime(user_bday.year,user_bday.month,user_bday.day)
    age_year = now.year - user_bday.year
    age_months = now.month - user_bday.month
    age_days = now.day - user_bday.day
    if age_days < 0:
        age_months -= 1
        age_days +=30
    if age_months < 0:
        age_year -=1
        age_months +=12
    next_bday = datetime.datetime(now.year, user_bday.month, user_bday.day)
    if next_bday < now:
        next_bday = datetime.datetime(now.year + 1, user_bday.month, user_bday.day)
    days_until = (next_bday - now).days
    if days_until == 0 or days_until == 365:
        print('Happy Birthday!')
    if gap.days <=0:
        print ("if you really are from the future")
    elif gap.days < 365:
        print (f"you are only {age_months} Months and {age_days} days old")
    else:
        print(f"you are approximately {age_year} years, {age_months} months and {age_days} days old")
    print(user_bday.strftime('you were born on a %A'))
    print(f'your next Birthday is in {days_until + 1} days')

def between_dates():
    print('enter the first date')
    date1 = vali_date()
    print(date1)
    print('enter the second date')
    date2 = vali_date()
    print(date2)
    date1 = datetime.datetime.strptime(date1, '%m/%d/%Y')
    date2 = datetime.datetime.strptime(date2, '%m/%d/%Y')
    if date1 < date2:
        print(f"the first date entered comes before the second")
        days_between = datetime.datetime(date2.year,date2.month,date2.day) - datetime.datetime(date1.year,date1.month,date1.day)
        older = date1
        younger = date2
    if date1 > date2:
        print(f"the second date entered comes before the first")
        days_between = datetime.datetime(date1.year,date1.month,date1.day) - datetime.datetime(date2.year,date2.month,date2.day)
        older = date2
        younger = date1
    if date1 == date2:
        print('its the same day')
        return
    year_diff = younger.year - older.year
    month_diff = older.month - younger.month
    day_diff = older.day - younger.day
    if day_diff < 0:
        month_diff -= 1
        day_diff +=30
    if month_diff < 0:
        year_diff -=1
        month_diff +=12
    print(f"there are {days_between.days} days between the two dates")
    print(f"or approximately {year_diff} years, {month_diff} months and {day_diff} days apart")
    print(f"the first date was on a {date1.strftime('%A')}")
    print(f"the second date was on a {date2.strftime('%A')}")

while True:
    try:
        choice = int(input("""Age / Date Calculator
    would you like to
    1. See Your Birthday statistics
    2. Calculate time between 2 dates

    9. Quit
    """))
        if choice == 1:
            bday_stats()
            continue
        elif choice == 2:
            between_dates()
            continue
        elif choice == 9:
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue























