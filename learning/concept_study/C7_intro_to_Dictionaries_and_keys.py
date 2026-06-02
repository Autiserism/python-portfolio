my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
my_cat['size']
'fat'
'My cat has ' + my_cat['color'] + ' fur.'

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
spam[12345]
'Luggage Combination'
spam[42]
'The Answer'
#spam[0]
KeyError: 0

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon  # The order of list items matters.
False
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham  # The order of dictionary key-value pairs doesn't matter.
True


spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

'color' in spam.keys()
True
'age' not in spam.keys()
False
'red' in spam.values()
True
for i in spam.items():
    print(i)

'color' in spam
True
'color' in spam.keys()
True

spam = {'color': 'red', 'age': 42}
spam.keys()  # Returns a list-like dict_keys value
#dict_keys(['color', 'age'])
list(spam.keys())  # Returns an actual list value
['color', 'age']

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + str(k) + ' Value: ' + str(v))


picnic_items = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
'I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')  # Sets 'color' key to 'black'
'black'
spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
spam.setdefault('color', 'white')  # Does nothing
'black'
spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))
