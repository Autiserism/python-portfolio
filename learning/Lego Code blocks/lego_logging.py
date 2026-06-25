# ======================================================================
# LEGO CODE BLOCKS — LOGGING
# lego_logging.py
# ======================================================================
# PURPOSE : Reusable logging setup and in-code log call patterns
# USE     : Open in Mu, find your block, copy what you need
# FILL-IN : Paste individual logging.X() lines throughout your code
#           wherever you'd want a print() during debugging
# ======================================================================
#
# LOGGING LEVELS — lowest to highest priority:
#
#   DEBUG    → fine-grained, step-by-step trace (start of func, loop var, etc.)
#   INFO     → general confirmation things are working as expected
#   WARNING  → something unexpected but the program still runs
#   ERROR    → a real problem — something didn't work
#   CRITICAL → program-breaking failure
#
#   basicConfig(level=logging.DEBUG) shows ALL levels.
#   basicConfig(level=logging.WARNING) shows only WARNING, ERROR, CRITICAL.
#   Higher level = fewer messages shown.
#
# FORMAT STRING TOKENS:
#   %(asctime)s   → timestamp
#   %(levelname)s → DEBUG / INFO / WARNING / etc.
#   %(message)s   → the text you passed to logging.debug() etc.
#
# ======================================================================


# ======================================================================
# REQUIRED IMPORTS — paste this at the top of your project file
# ======================================================================

import logging


# ======================================================================
# BLOCK LOG-1 — Basic Console Logging: Setup + All Level Examples
# ======================================================================
# DESCRIPTION : The standard logging setup for terminal-only output. Shows
#               timestamps, level name, and your message. Paste the
#               basicConfig line once at the top of your file, then drop
#               individual logging.X() calls wherever you need them.
#               Easier to disable than print() — one line turns it all off.
# FEEDS       : nothing — call logging.X() anywhere in your program
# RETURNS     : messages printed to the terminal while program runs
# TAGS        : logging, basicConfig, debug, info, warning, error, critical
# ======================================================================

# — Setup line — paste once at top of your file, above everything else
logging.basicConfig(
    level   = logging.DEBUG,   #<<<< change level to control what shows:
                               #     DEBUG=all | INFO | WARNING | ERROR | CRITICAL=least
    format  = '%(asctime)s  %(levelname)-8s  %(message)s'
    # %(levelname)-8s left-aligns the level name in an 8-char column so messages line up
)

# -----------------------------------------------------------------------
# — Individual log calls — copy these into your code wherever needed —
# -----------------------------------------------------------------------

logging.debug('Start of program')                             # step-by-step trace
logging.debug(f'variable value: {int_var1}')                 #<<<< swap int_var1

logging.info('File loaded successfully.')                     # general confirmation
logging.info(f'Loaded {int_var1} records.')                   #<<<< swap int_var1

logging.warning('No data found — using empty default.')       # unexpected but non-fatal
logging.warning(f'{string_var1} not found in data.')          #<<<< swap string_var1

logging.error('File does not exist.')                         # something failed
logging.error(f'Could not open {string_var1}')               #<<<< swap string_var1

logging.critical('Unrecoverable error — shutting down.')      # program-breaking

# -----------------------------------------------------------------------
# — Logging inside a function (common pattern)
# -----------------------------------------------------------------------

def function_name(param_var1):            #<<<< rename function and param
    logging.debug(f'function_name called with: {param_var1}')
    # ... your code here ...
    logging.debug(f'function_name returning: {param_var1}')
    return param_var1

# -----------------------------------------------------------------------
# — Logging inside a loop (track each iteration)
# -----------------------------------------------------------------------

for i, item in enumerate(list_var1):     #<<<< rename list_var1
    logging.debug(f'loop iteration {i}: {item}')


# ======================================================================
# BLOCK LOG-2 — Logging Inside try / except
# ======================================================================
# DESCRIPTION : Wraps a risky operation in try/except and logs what
#               happens at each stage. Log the attempt at DEBUG, success
#               at INFO, and the error at ERROR so you can see exactly
#               where things broke without a traceback wall of text.
# FEEDS       : any code that might raise an exception
# RETURNS     : log messages at each stage; program keeps running on error
# TAGS        : logging, try, except, error, exception, debug
# ======================================================================

def safe_operation(param_var1):   #<<<< rename function and param
    logging.debug(f'Attempting operation with: {param_var1}')
    try:
        result = param_var1       #<<<< replace with your actual operation
        logging.info(f'Operation succeeded: {result}')
        return result
    except ValueError as e:
        logging.error(f'ValueError in safe_operation: {e}')
        return None
    except Exception as e:
        logging.error(f'Unexpected error in safe_operation: {e}')
        return None

# — try/except with multiple exception types + final logging
try:
    value = float(input('Enter a number: '))
    logging.debug(f'User entered: {value}')
    result = 100 / value
    logging.info(f'Result: {result}')
except ValueError:
    logging.error('Input was not a valid number.')
except ZeroDivisionError:
    logging.warning('Division by zero attempted.')
except Exception as e:
    logging.critical(f'Unhandled exception: {e}')


# ======================================================================
# BLOCK LOG-3 — Disable All Logging
# ======================================================================
# DESCRIPTION : Silences every logging call in the program without
#               deleting them. Paste this one line when your program is
#               done being debugged and you want clean output.
#               To re-enable: remove or comment out this line.
# FEEDS       : nothing
# RETURNS     : all logging.X() calls become silent no-ops
# TAGS        : logging, disable, silence, production, turn off
# ======================================================================

logging.disable(logging.CRITICAL)   # silences everything at CRITICAL and below = all levels

# To re-enable all logging, set it back:
# logging.disable(logging.NOTSET)


# ======================================================================
# BLOCK LOG-4 — Save Logs to a File
# ======================================================================
# DESCRIPTION : Writes all log messages to a .log file on disk instead of
#               (or in addition to) the terminal. Useful for programs that
#               run without you watching, or when you want a record after
#               the program exits. Use mode='w' to overwrite each run, or
#               mode='a' to accumulate across runs.
# FEEDS       : nothing — logging.X() calls work the same
# RETURNS     : a .log file written to your project folder
# TAGS        : logging, file, save, FileHandler, log file, persist
# ======================================================================

from pathlib import Path

log_dir  = Path.home() / 'projects' / >'foldername'<   #<<<< match your project folder
log_path = log_dir / >'logfile.log'<                    #<<<< name your log file

logging.basicConfig(
    filename = log_path,
    filemode = 'w',                     #<<<< 'w'=overwrite each run | 'a'=append across runs
    level    = logging.DEBUG,
    format   = '%(asctime)s  %(levelname)-8s  %(message)s'
)

# — Log calls below work exactly the same — output goes to the file
logging.debug('Program started.')
logging.info('Setup complete.')
logging.warning('Something to watch.')
logging.error('Something went wrong.')


# ======================================================================
# BLOCK LOG-5 — Dual Handler: Log to Both Terminal and File Simultaneously
# ======================================================================
# DESCRIPTION : The most complete setup — sends log messages to the
#               terminal AND saves them to a file at the same time.
#               Use different levels per handler: e.g. DEBUG to terminal
#               (verbose) and INFO to file (cleaner saved record).
#               NOTE: Do NOT use basicConfig() when adding handlers manually
#               — set up the root logger directly instead.
# FEEDS       : nothing — logging.X() calls work the same
# RETURNS     : messages shown in terminal + saved to log file
# TAGS        : logging, dual, handler, FileHandler, StreamHandler, both
# ======================================================================

import sys
from pathlib import Path

log_dir  = Path.home() / 'projects' / >'foldername'<   #<<<< match your project folder
log_path = log_dir / >'logfile.log'<                    #<<<< name your log file

# — Shared format
formatter = logging.Formatter('%(asctime)s  %(levelname)-8s  %(message)s')

# — Terminal handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)     #<<<< level for terminal output
console_handler.setFormatter(formatter)

# — File handler
file_handler = logging.FileHandler(log_path, mode='w')   #<<<< 'w'=overwrite | 'a'=append
file_handler.setLevel(logging.INFO)                       #<<<< level for file output (can differ)
file_handler.setFormatter(formatter)

# — Attach both to the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)   # master level — must be lowest of the two handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# — Log calls below go to both terminal and file
logging.debug('This shows in terminal only (below INFO).')
logging.info('This shows in both terminal and file.')
logging.warning('This shows in both.')
logging.error('This shows in both.')
