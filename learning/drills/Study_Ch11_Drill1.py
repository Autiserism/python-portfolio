'''
Drill 1
Write a program that:
name
Creates a folder called backup in your Documents folder
Copies all .py files from your python_portfolio/projects folder into the backup folder
Prints how many files were copied

Use shutil.copy() and glob().
'''

from pathlib import Path
import shutil,os
file_path = Path.home()
data_dir = file_path / 'Documents' / 'python_portfolio'# / 'projects' / 'basic_programs'
(file_path / 'projects' / 'python_projects_backup2').mkdir(exist_ok=True)
amount = 0
#for f in data_dir.glob('*.py'):
    #amount +=1

#print(f"{amount} files were backed up")



for filepath, subfolders,files in os.walk(data_dir):
    print("Current folder is ", filepath)
    for subfolder in subfolders:
        print("     its in sub", subfolder)
    for file in files:
        print("         file is ", file)
        if file.endswith('.py'):
            shutil.copy(files,  file_path / 'python_projects_backup2')
            amount +=1











