'''
Nested dictionary update
Write a program that stores three employees
each with a name and a dictionary of monthly sales figures for January, February and March.
Write functions to update a monthly figure and recalculate the total.
Use find_employee() helper and update nested values directly.
'''

employees = {
'emp1': { 'name':'Quimba', 'sales':{'January': 100, 'February': 125, 'March': 110 }},
'emp2' : { 'name':'1', 'sales':{'January': 111, 'February': 150, 'March': 99 }},
'emp3' : { 'name':'Zeewee', 'sales':{'January': 109, 'February': 124, 'March': 122 }}
}
total_sold = 0
def total_sales():
    global total_sold
    for enum, file in employees.items():
        total_sold += sum(file['sales'].values())
    print(f"total sales across {len(file['sales'])} Months: {total_sold}")
total_sales()

def find_employee(name):
    for emp_id, emp_data in employees.items():
        if emp_data['name'].lower() == name.lower():
            return emp_data
    return None
    #print (f"Name: {empdata[0]['name']} \nTotal Sales: {sum(empdata[0]['sales'].values())}")

def update_rec():
    name = input("enter their name: ").title()
    record = find_employee(name)
    if record is None:
        print('not found')
        return
    months = list(record['sales'].keys())
    for i,mon in enumerate(months,1):
        print(f"{i} {mon} {record['sales'][mon]}")
    try:
        choice = int(input('enter the month #')) -1
        selected_mon = months[choice]
        record['sales'][selected_mon] = int(input("Enter the updated total: "))
        print(f"{record['name']} sales for {selected_mon} has been updated")
        for i, mon in enumerate(months, 1):
            print(f"{i}. {mon}: {record['sales'][mon]}")
        total_sales()
        return
    except ValueError:
        print('input a #')
        return
    except IndexError:
        print('a month on the list')
        return

#name = input('>').title()
result = update_rec()
#print(employees)
#

#1
#sum(subjects.values()) → 255


#for i, mun in enumerate(monthly, 1):
#            print(f"{i} {mun}")


