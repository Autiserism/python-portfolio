DESIGNING AND DEPLOYING COMMAND LINE PROGRAMS
**********************************************************************
'Running Python Scripts from the Terminal
//////////////////////////////////////////////////////////////////////
What it is:
    Instead of using Mu to run scripts,
    you can run them directly from your operating systems terminal by typing python
    yourScript.py (Windows) or python3 yourScript.py (macOS/Linux).
    The terminal needs to either be in the same folder as the script, or you pass the full absolute path to it.

Why it matters:
    Lets you run programs quickly without opening a code editor,
    and is the foundation for everything else in this chapter.

Example:
# Windows - from the script's folder
python yourScript.py

# macOS/Linux - from the script's folder
python3 yourScript.py

# From anywhere using absolute path
python C:\Users\Al\Scripts\yourScript.py
Key terminal commands:
cd foldername     # change directory
cd ..             # go up one level
dir               # list folder contents (Windows)
ls                # list folder contents (macOS/Linux)
pwd               # print working directory (macOS/Linux)
cd                # print working directory (Windows)

Gotcha:
    On macOS and Linux, to run a script in the current folder you must write ./scriptname not just scriptname
    the terminal wont check the current folder unless you explicitly reference it.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'The PATH Environment Variable
//////////////////////////////////////////////////////////////////////
What it is:
    PATH is a list of folders your terminal checks when you type a command name.
    When you type python, the terminal searches each folder in PATH until it finds a program with that name and runs it.
    Adding your Scripts folder to PATH means you can run your own scripts from anywhere without typing the full path.

Why it matters:
    Without your Scripts folder in PATH,
    youd have to cd into that folder every time you want to run your scripts.

Example:
# Check PATH contents:
echo %PATH%          # Windows
echo $PATH           # macOS/Linux

# Find where a program is located:
where python         # Windows
which python3        # macOS/Linux

Gotcha:
    PATH doesnt search subfolders — if C:\Users\Al\Scripts is in PATH, a script in C:\Users\Al\Scripts\tools\
    wont be found unless that subfolder is also in PATH.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Virtual Environments — venv
//////////////////////////////////////////////////////////////////////
What it is:
    A virtual environment is an isolated Python installation with its own separate set of installed packages.
    You create one using Pythons built-in venv module, then activate it to use it — after activation,
    any packages you install go into that environment only, not your main Python installation.

Why it matters:
    Prevents package version conflicts between projects,
    and keeps third-party installs from potentially breaking your system Python.

Example:
# Create virtual environment in a folder called .venv
python -m venv .venv             # Windows
python3 -m venv .venv            # macOS/Linux

# Activate
.venv\Scripts\activate.bat       # Windows
source .venv/bin/activate        # macOS/Linux

# Prompt changes to show (.venv) when active
(.venv) C:\Users\Al\Scripts>

# Deactivate
deactivate

Gotcha:
    Activating a virtual environment only affects the current terminal window
    new terminal windows still use system Python until you activate again.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'pip — Installing Third-Party Packages
//////////////////////////////////////////////////////////////////////
What it is:
    pip is Pythons built-in package manager that downloads and installs packages from PyPI (Python Package Index).
    Always run it through the Python interpreter using python -m pip rather than calling pip directly
    this ensures youre installing to the correct Python installation.

Why it matters:
    The entire ecosystem of third-party packages (pyperclip, requests, pandas, etc.) is installed through pip.

Example:
# Install a package
python -m pip install pyperclip         # Windows
python3 -m pip install pyperclip        # macOS/Linux

# List installed packages
python -m pip list

# Install specific version
python -m pip install pyperclip==1.8.2

# Upgrade a package
python -m pip install -U pyperclip

# Uninstall
python -m pip uninstall pyperclip

Gotcha:
    Running pip install without python -m can install to the wrong Python version if you have multiple Python installations
    always use python -m pip.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'sys.argv — Reading Command Line Arguments
//////////////////////////////////////////////////////////////////////
What it is:
    When you run a Python script from the terminal,
    any extra words typed after the filename are passed to your script through the sys.argv list.
    The first item is always the script filename itself; anything after it are your arguments as strings.

Why it matters:
    Lets users configure your programs behavior at launch without changing the source code
    like flags and options on built-in terminal commands.

Example:
import sys

# Run as: python myScript.py hello world
print(sys.argv)            # ['myScript.py', 'hello', 'world']
print(sys.argv[0])         # 'myScript.py'
print(sys.argv[1])         # 'hello'

# Practical use — change behavior based on argument
if len(sys.argv) > 1:
    density = int(sys.argv[1])
else:
    density = 4   # default

Gotcha:
    All arguments in sys.argv are strings
    if youre expecting a number, you must convert it with int() or float() yourself.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Self-Aware Python Variables
//////////////////////////////////////////////////////////////////////
What it is:
    Python automatically sets several built-in variables
    that give your script information about itself and the environment its running in
    things like its own file path, the Python version, and what OS its running on.
    These are read-only and set by the interpreter at runtime.

Why it matters:
    Lets your script adapt to different environments or locate files relative to itself without hardcoding paths.

Key variables at a glance:

__file__                            — the scripts own filepath as a string
sys.executable                      — full path to the Python interpreter running this script
sys.version                         — Python version as a readable string
sys.version_info.major / .minor     — version numbers as integers (e.g. 3, 13)
os.name                             — 'nt' on Windows, 'posix' on macOS/Linux
sys.platform                        — 'win32', 'darwin', or 'linux'

Example:
import sys, os
from pathlib import Path

print(__file__)                        # 'C:/Users/Al/Scripts/myScript.py'
print(Path(__file__).parent)          # useful for locating files near the script

print(sys.version_info.major)         # 3
print(sys.version_info.minor)         # 13
print(os.name)                        # 'nt' on Windows

# Run different code per OS
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

Gotcha:
    __file__ does not exist when running code in the Python interactive shell
    only works in scripts run from a file.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'bext — Colored Terminal Text and Cursor Control
//////////////////////////////////////////////////////////////////////
What it is:
    bext is a third-party package that adds color and basic cursor positioning to terminal output.
    You call fg() to set the text (foreground) color and bg() to set the background color using color name strings,
    then use print() as normal — the color applies until you reset it.

Why it matters:
    Lets you add visual emphasis to terminal output without needing a full GUI.

Functions at a glance:

bext.fg('color')                — sets text color; pass 'reset' to restore default
bext.bg('color')                — sets background color; pass 'reset' to restore default
bext.clear()                    — clears the terminal screen
bext.goto(x, y)                 — moves cursor to column x, row y (0,0 is top-left)
bext.width() / bext.height()    — returns terminal width/height in characters
bext.get_key()                  — waits for a keypress and returns it as a string

Example:
import bext

bext.fg('red')
print('This is red text.')

bext.bg('blue')
print('Red text on blue background.')

bext.fg('reset')
bext.bg('reset')
print('Back to normal.')
Gotcha:
    bext only works when run from a terminal
    it wont produce colors inside Mu or most code editors.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'PyMsgBox — Simple GUI Popup Dialogs
//////////////////////////////////////////////////////////////////////
What it is:
    PyMsgBox is a third-party package that creates small GUI dialog boxes
    alerts, confirmations, and text input prompts — without building a full GUI application.
    Each function blocks until the user clicks a button, then returns their response as a string.

Why it matters:
    Adds a simple interactive layer to scripts that otherwise run silently in the terminal,
    without requiring a full GUI framework.

Functions at a glance:

pymsgbox.alert(text)    — shows a message, returns 'OK' when dismissed
pymsgbox.confirm(text)  — shows OK/Cancel, returns 'OK' or 'Cancel'
pymsgbox.prompt(text)   — shows a text field, returns the typed string or None
pymsgbox.password(text) — same as prompt but input is masked with asterisks

Example:
import pymsgbox

pymsgbox.alert('Task complete!')
choice = pymsgbox.confirm('Continue?')   # 'OK' or 'Cancel'
name = pymsgbox.prompt('Enter your name:')

Gotcha:
    All PyMsgBox functions block program execution until the user responds
    dont call them inside a time-sensitive loop.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'PyInstaller — Compiling Scripts to Executables
//////////////////////////////////////////////////////////////////////
What it is:
    PyInstaller packages your Python script and a copy of the Python interpreter
    into a single standalone executable file that can run on computers without Python installed.
    The resulting file is large (often several MB) but requires no setup from the recipient.

Why it matters:
    Lets you share finished programs with non-programmers who dont have Python or any packages installed.

Example:
# Install
python -m pip install pyinstaller

# Compile (note capital P and I)
python -m PyInstaller --onefile yourScript.py
The executable ends up in the dist/ folder. The build/ folder can be deleted.

Gotcha:
    PyInstaller builds for the OS youre currently on
    a Windows executable must be compiled on Windows; you cant cross-compile for a different platform.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Deployment — Batch Files and Shell Scripts
//////////////////////////////////////////////////////////////////////
What it is:
    A batch file (.bat on Windows) or shell script (.command on macOS, no extension on Linux)
    is a small text file containing terminal commands that runs your Python script.
    Placing these launcher files in your PATH folder means you can run your programs by name from anywhere.

Why it matters: Turns a multi-step "open editor → load file → click run"
process into a single command you can type in two seconds.

Windows .bat template:
bat@call %HOMEDRIVE%%HOMEPATH%\Scripts\.venv\Scripts\activate.bat
@python %HOMEDRIVE%%HOMEPATH%\Scripts\yourScript.py %*
@pause
@deactivate
macOS .command template:
bashsource ~/Scripts/.venv/bin/activate
python3 ~/Scripts/yourScript.py
deactivate

Then run: chmod u+x yourScript.command to make it executable.

Linux shell script template:
bash#!/usr/bin/env bash
source ~/Scripts/.venv/bin/activate
python3 ~/Scripts/yourScript.py
read -p "Press any key to continue..." -n1 -s
deactivate
Then run: chmod u+x yourScript to make it executable.

Gotcha:
    On Windows, batch files that call other batch files (like activate.bat)
    must use the call keyword without it,
    execution stops after the called file finishes and your script never runs.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
Summary:
//////////////////////////////////////////////////////////////////////
Run scripts from terminal with python script.py; add your Scripts folder to PATH so you can run them from anywhere

sys.argv passes command line arguments to your script as a list of strings — index 0 is always the script name

Create a .venv virtual environment per project with python -m venv .venv; always use python -m pip to install packages to the right environment

Self-aware variables (__file__, os.name, sys.platform, sys.version_info) let scripts adapt to their environment at runtime

bext adds terminal colors and cursor control; PyMsgBox adds simple popup dialogs — both are lightweight alternatives to full GUI frameworks

Deployment = a .bat/.command/shell script launcher in your PATH folder that activates the venv, runs the script, and deactivates

PyInstaller --onefile bundles a script into a shareable executable — must be compiled on the target OS
