import pyperclip, time,json, os,datetime
from pathlib import Path

data_dir = Path.home() / 'research'
data_dir.mkdir(parents=True, exist_ok=True)
os.chdir(data_dir)

file_path = data_dir / >'filename.txt'< #<<<<<<<<<< set file name
now = datetime.datetime.now()

string_var1 = f'{now}\n' #<<<<<<<<<<<<<< if making a file set starting note

if file_path.exists():
    pass
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(string_var1)


print('Recording clipboard... (Ctrl-C to stop)')
previous_content = ''
try:
    while True:
        content = pyperclip.paste()  # Get clipboard contents. requires the pyperclip add on
        if content != previous_content:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(f'\n{content}')
            print(content)
            previous_content = content

        time.sleep(5.00)  # Pause in seconds to avoid hogging the CPU.
except KeyboardInterrupt:
    pass




