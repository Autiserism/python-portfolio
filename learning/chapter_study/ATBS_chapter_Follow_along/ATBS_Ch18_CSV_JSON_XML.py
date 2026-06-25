import csv , os
from pathlib import Path
os.chdir(Path.home() / 'projects' / 'EX3ATBS')
#print(Path.cwd())

example_file = open('exampleWithHeader3.csv')
example_reader = csv.reader(example_file)
#example_data = list(example_reader)
#print(example_data)

'''
Reading CSV Files

print(example_data[0][0]) # first row, first column
print(example_data[0][1]) # first row, second column
print(example_data[0][2]) # first row, third column
print(example_data[1][2]) # second row, third column
'''

'''
Accessing Data in a for Loop

#(comment out example_data for the print to work)
for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))
'''

'''
Writing CSV Files

output_file = open('output.csv', 'w' , newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
'''

'''
Handling Header Rows


'''
import csv
example_file = open('exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)
#example_dict_data = list(example_dict_reader) #<<<<comment out for row print to work
#print(example_dict_data)
for row in example_dict_reader:
    print(row['Timestamp'],row['Fruit'],row['Quantity'].rjust(10,chr(333)))









example_file.close()

