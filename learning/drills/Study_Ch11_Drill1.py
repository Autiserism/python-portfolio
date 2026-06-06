'''
Drill 1
Write a program that:

Creates a folder called backup in your Documents folder
Copies all .py files from your python_portfolio/projects folder into the backup folder
Prints how many files were copied

Use shutil.copy() and glob().
'''

from pathlib import Path
import shutil
file_path = Path.home()
data_dir = file_path / 'Documents' / 'python_portfolio' / 'projects' / 'basic_programs'
(file_path / 'python_projects_backup').mkdir(exist_ok=True)
amount = 0
for f in data_dir.glob('*.py'):
    amount +=1
    shutil.copy(f,  file_path / 'python_projects_backup')
print(f"{amount} files were backed up")















