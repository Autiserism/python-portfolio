'''
    Dynamic dictionary building
Write a program that asks the user how many categories they want to track.
Then asks for a name and value for each category.
Builds a dictionary dynamically from the input.
Calculate and display the total and average of all values.
'''

dynamic_dictionary = {}

choice = int(input("enter # categories to track: "))
for i in range(choice):
    name = input('k: ')
    value = int(input('v: '))
    dynamic_dictionary.update({i+1 : {'category': name, 'value': value}})
    print(f"{name}, {value} Added")
print(dynamic_dictionary)

total = 0
for i, track in dynamic_dictionary.items():
    print(track['value'])
    total += track['value']

total /= len(dynamic_dictionary)
print(total)


#for i in range(len(dynamic_dictionary)):
#    print(sum(dynamic_dictionary[i]['value']) / len(dynamic_dictionary[i]['value']) )



















