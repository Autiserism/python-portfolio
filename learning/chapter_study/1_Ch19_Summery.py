KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS
***********************************************
'time.time() and time.ctime() — Epoch Timestamps
//////////////////////////////////////////////////////////////////////
What it is:
    The Unix epoch is a fixed reference point in time — midnight January 1, 1970 UTC.
    time.time() returns a float representing how many seconds have passed since that moment,
    called an epoch timestamp. time.ctime() converts that number into a human-readable string.

Why it matters:
    Epoch timestamps are how Python tracks and measures time internally —
    you can use them to measure how long code takes to run,
    or as a reference point for scheduling.

Functions at a glance:

time.time() — returns the current moment as a float (seconds since epoch)
time.ctime() — returns the current time as a readable string; optionally accepts an epoch float

Example:

import time

time.time()             # 1773813875.35  (raw epoch float)
time.ctime()            # 'Tue Mar 17 11:05:38 2026'

# Profiling code speed
start = time.time()
# ...some code...
end = time.time()
print(f'Took {end - start} seconds')

Gotcha:
    time.time() returns a float with many decimal places —
    use round() when displaying elapsed time to keep output readable.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'time.sleep() — Pausing Execution
//////////////////////////////////////////////////////////////////////
What it is:
    time.sleep() halts your program for a specified number of seconds before continuing.
    It completely blocks execution — nothing else in your script runs during the pause.

Why it matters:
    Essential for rate-limiting loops, creating delays between actions,
    and building any program that needs to wait before checking or acting again.

Example:

import time

for i in range(3):
    print('Tick')
    time.sleep(1)     # pause 1 second
    print('Tock')
    time.sleep(1)

# Pause until a specific date by combining with a while loop
import datetime
target = datetime.datetime(2027, 1, 1, 0, 0, 0)
while datetime.datetime.now() < target:
    time.sleep(1)     # check once per second instead of hammering the CPU

Gotcha:
    time.sleep() blocks the entire program — no other code runs during the pause.
    If you need other tasks to continue running, youd need threads or async code (beyond this chapters scope).
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'datetime Module — Working with Dates and Times
//////////////////////////////////////////////////////////////////////
What it is:
    The datetime module provides a datetime object that stores a specific moment in time
    as individual components — year, month, day, hour, minute, second —
    all accessible as attributes. You can create them for the current moment
    or any specific date and compare them directly with >, <, and ==.

Why it matters:
    Epoch floats are hard to work with for human-scale date math — datetime objects let you compare dates,
    extract components, and do arithmetic naturally.

Functions at a glance:

datetime.datetime.now() — returns a datetime object for the current moment
datetime.datetime(y, m, d, h, min, s) — creates a datetime for a specific moment
datetime.datetime.fromtimestamp(epoch) — converts an epoch float to a datetime object

Example:

import datetime

now = datetime.datetime.now()
print(now.year, now.month, now.day)     # 2026, 3, 17
print(now.hour, now.minute, now.second) # 11, 5, 38

# Specific moment
halloween = datetime.datetime(2026, 10, 31, 0, 0, 0)

# Comparison
new_year = datetime.datetime(2027, 1, 1, 0, 0, 0)
new_year > halloween    # True — later date is "greater"

# Convert epoch to datetime
import time
datetime.datetime.fromtimestamp(time.time())   # same as datetime.now()

Gotcha:
    datetime.datetime.now() is called on the class itself, not an instance —
    its easy to accidentally write datetime.now() and get an AttributeError
    because you forgot the double datetime.datetime.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'timedelta — Representing and Doing Date Arithmetic
//////////////////////////////////////////////////////////////////////
What it is:
    A timedelta object represents a duration of time rather than a specific moment.
    You create one by passing keyword arguments for weeks, days, hours, minutes,
    and seconds, then add or subtract it from a datetime object to get a new date.

Why it matters:
    Lets you answer questions like "what date is 90 days from now?" or "how many days between two dates?"
    without manually counting months and leap years.

Functions/methods at a glance:

datetime.timedelta(days, hours, minutes, seconds, weeks) — creates a duration object
.total_seconds() — returns the total duration expressed as a single float in seconds
str(timedelta) — returns a human-readable string like '11 days, 10:09:08'

Example:

import datetime

# Create a duration
delta = datetime.timedelta(days=30, hours=6)
delta.days            # 30
delta.total_seconds() # 2613600.0
str(delta)            # '30 days, 6:00:00'

# Date arithmetic
now = datetime.datetime.now()
future = now + datetime.timedelta(days=100)   # 100 days from now
past = now - datetime.timedelta(weeks=4)      # 4 weeks ago

# Difference between two dates returns a timedelta
gap = datetime.datetime(2027, 1, 1) - datetime.datetime.now()
print(gap.days)       # days until new year

Gotcha:
    timedelta has no months or years argument —
    those would be variable-length durations. Use days=365 as an approximation,
    but be aware it ignores leap years.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'strftime() and strptime() — Converting Between Dates and Strings
//////////////////////////////////////////////////////////////////////
What it is:
    strftime() formats a datetime object into a custom string using format codes like %Y for year and %m for month.
    strptime() does the reverse — it parses a date string into a datetime object using the same format codes.
    Both use the same set of directives.

Why it matters:
    Real-world date data comes in strings from files, user input, and APIs —
    strptime() converts them to objects you can do math on, and strftime() converts them back to display nicely.

Key format codes:
Code            Meaning             Example
%Y              4-digit year         2026
%y              2-digit year          26
%m              Month number          10
%B              Full month name     October
%d              Day of month          21
%H              Hour (24h)            16
%I              Hour (12h)            04
%M              Minute                29
%S              Second                00
%p              AM/PM                 PM
%A              Full weekday        Monday

Example:

import datetime

dt = datetime.datetime(2026, 10, 21, 16, 29, 0)

# datetime → string
dt.strftime('%Y/%m/%d')          # '2026/10/21'
dt.strftime('%I:%M %p')          # '04:29 PM'
dt.strftime('%A, %B %d, %Y')     # 'Wednesday, October 21, 2026'

# string → datetime
datetime.datetime.strptime('2026/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
# datetime.datetime(2026, 10, 21, 16, 29)

datetime.datetime.strptime('October 21, 2026', '%B %d, %Y')
# datetime.datetime(2026, 10, 21, 0, 0)

Using the datetime module, what day of the week was January 7, 2019?
import datetime
d = datetime.datetime(2019, 1, 7)
print(d.strftime('%A'))  # prints 'Monday'
Or using .weekday() which returns a number — 0 is Monday, 6 is Sunday:

d.weekday()  # returns 0 (Monday)
strftime() format codes worth memorizing for M1P3:

'%Y'  # 2026 — four digit year
'%m'  # 06 — month as number
'%d'  # 15 — day as number
'%A'  # Monday — full weekday name
'%B'  # June — full month name
'%H'  # 14 — hour (24hr)
'%I'  # 02 — hour (12hr)
'%M'  # 00 — minutes
'%p'  # PM — AM/PM

And strptime() for converting user input to datetime:
datetime.datetime.strptime('06/10/2025', '%m/%d/%Y')


Gotcha:
    strptime() is a class method called on datetime.datetime, not on an instance —
    and the format string must match the input string exactly or Python raises a ValueError.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'subprocess.run() — Launching Other Programs
//////////////////////////////////////////////////////////////////////
What it is:
    subprocess.run() from the subprocess module launches an external program from inside your Python script.
    You pass it a list where the first item is the executable path
    and any remaining items are command line arguments. The function blocks —
    your Python script pauses and waits until the launched program closes.

Why it matters:
    Lets your Python script trigger other programs, open files, or run terminal commands without you having to do it manually.

Example:

import subprocess

# Launch a program (blocks until closed)
subprocess.run(['C:\\Windows\\System32\\calc.exe'])   # Windows
subprocess.run(['/usr/bin/gnome-calculator'])          # Linux
subprocess.run(['open', '/System/Applications/Calculator.app'])  # macOS

# Pass command line arguments
subprocess.run(['C:\\Windows\\notepad.exe', 'C:\\Users\\Al\\hello.txt'])

# Capture terminal command output
proc = subprocess.run(['ping', '-n', '4', 'google.com'], capture_output=True, text=True)
print(proc.stdout)   # the text output of ping as a string

Gotcha:
    On macOS, you must use the open command and pass the .app as an argument —
    you cant run .app bundles directly with subprocess.run().
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'subprocess.Popen() — Launching Without Blocking
//////////////////////////////////////////////////////////////////////
What it is:
    subprocess.Popen() launches an external program just like run(),
    but returns immediately without waiting for the program to close.
    It returns a Popen object that you can use to monitor or control the running process.

Why it matters:
    Use this when you want your Python script to continue doing other work while the launched program runs in the background.

Methods at a glance:

.poll() — checks if the process has ended; returns None if still running, or an integer exit code if done
.wait() — blocks until the process finishes; returns the exit code
.kill() — immediately terminates the process with no confirmation

Example:

import subprocess

# Launch without blocking
proc = subprocess.Popen(['C:\\Windows\\System32\\mspaint.exe'])

proc.poll()    # None — still running
               # 0    — finished without errors

proc.wait()    # blocks until MS Paint is closed, then returns exit code

proc.kill()    # force-closes immediately — any unsaved work is lost

Gotcha:
    kill() terminates the process instantly with no save prompt or confirmation —
    unsaved data in the killed program is gone.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Opening Files with Their Default Application
//////////////////////////////////////////////////////////////////////
What it is:
    You can open any file using whatever application the OS has associated with that file type —
    the same behavior as double-clicking it —
    by passing 'start' (Windows) or 'open' (macOS/Linux) to subprocess.run() along with the file path.

Why it matters:
    Your script doesnt need to know which app to use —
    the OS figures that out, so a .pdf opens in a PDF viewer, a .wav plays in the audio app, and so on.

Example:

import subprocess

# Windows — requires shell=True
subprocess.run(['start', 'report.pdf'], shell=True)
subprocess.run(['start', 'alarm.wav'], shell=True)

# macOS and Linux
subprocess.run(['open', 'report.pdf'])
subprocess.run(['open', 'alarm.wav'])

Gotcha:
    On Windows, shell=True is required when using 'start' —
    without it youll get a FileNotFoundError because start is a shell command, not a standalone executable.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Summary:
//////////////////////////////////////////////////////////////////////
time.time() returns an epoch float; time.ctime() converts it to a readable string; time.sleep(n) pauses execution for n seconds

datetime.datetime objects store a specific moment with named attributes (.year, .month, .day, etc.) and support direct comparison with >, <, ==

timedelta represents a duration — add/subtract it from datetime objects to do date arithmetic;
use .total_seconds() for the full duration as a number

strftime() converts a datetime to a formatted string;
strptime() parses a formatted string back into a datetime — both use the same format codes (%Y, %m, %d, etc.)

subprocess.run() launches a program and blocks until it closes;
subprocess.Popen() launches without blocking — use .poll(), .wait(), and .kill() to manage the running process

Pass 'start' (Windows, with shell=True) or 'open' (macOS/Linux) to subprocess.run() to open any file with its default application
