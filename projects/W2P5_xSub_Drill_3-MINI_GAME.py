'''
Transaction/history log pattern
Write a program that manages a simple points system. Users can earn points, spend points and view history.
Every action appends to a history list with a timestamp using
import datetime — datetime.datetime.now(). New concept but simple to use.
'''
import random, logging, datetime
logging.basicConfig(level=logging.DEBUG)
datetime.datetime.now()

history = []
pressure = 50
stall = 0
explode = 100
shift_hours_left = 12

def log_action(action, value, new_pressure):
    time = datetime.datetime.now()
    entry = f"{action} {value}, NP {new_pressure}, {time}, {shift_hours_left} to go"
    history.append(entry)
    logging.debug(entry)

def build_pressure():
    logging.debug("Build pressure initiated")
    global pressure, shift_hours_left
    time = datetime.datetime.now()
    little = random.randint(5, 20)
    some = random.randint(20, 50)
    alot = random.randint(50, 85)
    try:
        choice = int(input("Pull the Lever Cronk! \nBuild: \n1. A little \n2. Some \n3. Alot \n"))
        if choice == 1:
            pressure += little
            shift_hours_left -=1
            print(f"{little} pressure Built new pressure is {pressure}")
            log_action("Built", little, pressure)
            advance_time()
            return
        elif choice == 2:
            pressure += some
            shift_hours_left -=1
            print(f"{some} pressure built new pressure is {pressure}")
            log_action("Built", some, pressure)
            advance_time()
            return
        elif choice == 3:
            pressure += alot
            shift_hours_left -=1
            print(f"{alot} pressure built new pressure is {pressure}")
            log_action("Built", alot, pressure)
            advance_time()
            return
        else:
            print('is it your first day on the job ? its 1, 2 0r 3 ')
            pressure += little
            print(f"your inaction rose the pressure by {little}")
            log_action("Built", little, pressure)
            advance_time()
            return
    except ValueError:
        print("you fell flat on your face on your way to the lever \nLuckally (you think) no one saw it ")
        print("you check your watch you were knocked out cold for an hour!")
        print(f"Nap time rose the pressure by {little}")
        pressure += little
        log_action("Built", little, pressure)
        advance_time()
        return



def relive_pressure():
    logging.debug('relive pressure initiated')
    global pressure, shift_hours_left
    time = datetime.datetime.now()
    little = random.randint(5, 20)
    some = random.randint(20, 50)
    alot = random.randint(50, 85)
    try:
        choice = int(input("Pull the Lever Cronk! \nRelive: \n1. A little \n2. Some \n3. Alot \n"))
        if choice == 1:
            pressure -= little
            shift_hours_left -=1
            print(f"you log: {little} pressure relived new pressure is {pressure}")
            log_action("Relived", little, pressure)
            advance_time()
            return
        elif choice == 2:
            pressure -= some
            shift_hours_left -=1
            print(f"you log: {some} pressure relived new pressure is {pressure}")
            ("Relived", some, pressure)
            advance_time()
            return
        elif choice == 3:
            pressure -= alot
            shift_hours_left -=1
            print(f"you log: {alot} pressure relived new pressure is {pressure}")
            ("Relived", alot, pressure)
            advance_time()
            return
        else:
            print('is it your first day on the job ? its 1, 2 Or 3 ')
            pressure += little
            print(f"your inaction rose the pressure by {little}")
            log_action("Built", little, pressure)
            advance_time()
            return
    except ValueError:
        print("you fell flat on your face on your way to the lever \nLuckally (you think) no one saw it ")
        print("you check your watch you were knocked out cold for an hour!")
        print(f"Nap time rose the pressure by {little}")
        pressure += little
        log_action("Built", little, pressure)
        advance_time()
        return

def view_history():
    logging.debug("view_history initiated")
    for i in history:
        print(i)
    return

def advance_time():
    logging.debug("advance time initiated")
    global pressure, shift_hours_left
    shift_hours_left -=1
    faulty = random.randint(-45, 45)
    pressure += faulty
    time = datetime.datetime.now()
    log_action("1 hr down", faulty, pressure)
    print(f"you log: pressure variance {faulty} new pressure value {pressure}")
    print(f"{shift_hours_left} hours left on the clock")
    return

print("You are tasked with keeping the faulty equipment within range for your 12 hr shift while logging each action")
print("you clock in")
while True:
    if pressure <=0:
        print("life support terminated no pressure, no power")
        print("Fired")
        break
    if pressure >= 100:
        print("'Explosion'")
        print(" ")
        break
    if shift_hours_left <= -1:
        print("you clocked out its someone elses problem now")
        break
    try:
        choice = int(input(f"""the current pressure is {pressure} with {shift_hours_left} hours left on the clock
    would you like to
    1.Build pressure
    2.Relive pressure
    3.Wait an Hour
    4.View all logs
    9.Quit
    """))
        if choice == 1:
            build_pressure()
            continue
        elif choice == 2:
            relive_pressure()
            continue
        elif choice == 3:
            advance_time()
            continue
        elif choice == 4:
            view_history()
            continue
        elif choice == 9:
            pressure = 100
            print("you say screw this and begin to walk out")
            print("you hear a strange sound of pressure building then...")
            continue
        else:
            print("-Sips Coffee- \n(1,2,3 or 4)")
            continue
    except ValueError:
        print("if only you could count")
        print("pick an option")
        continue

logging.disable(logging.CRITICAL)















