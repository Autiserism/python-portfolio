'''
Drill A — Nested dictionary access
Create a dictionary of 3 products where each product has price, stock and category as nested keys.
Write functions to get a product's price, update its stock
and display all products in a formatted table.
'''

stocked_items = { 'milk' : { 'price': 5, 'stock' : 10, 'category' : 'dairy'},
 'beef' : { 'price': 25, 'stock' : 8, 'category' : 'meat'},
  'rice' : { 'price': 4, 'stock' : 30, 'category' : 'grain'},
}


def display_price(stocked_items):
    if not stocked_items:
        print('Famine')
        return
    for item_name in stocked_items.keys():
        print(f'{item_name}')
    item = input('which item for price: ')
    if item in stocked_items:
        price = stocked_items[item]['price']
        print(f'The price of {item} is ${price}')
    else:
        print('free if you run fast enough')
        return

def update_stock(stocked_items):
    for item_name in stocked_items.keys():
        print(f'{item_name}')
    item = input('Which item to restock? ')
    amount = int(input('How many to add? '))
    if item in stocked_items:
        stocked_items[item]['stock'] += amount
        print(f'New stock for {item}: {stocked_items[item]["stock"]}')
    else:
        print('Item not found')

def display_all(stocked_items):
    for item_name, item_data in stocked_items.items():
        print(f'\n{item_name}:')
        print(f'  Price: ${item_data["price"]}')
        print(f'  Stock: {item_data["stock"]}')
        print(f'  Category: {item_data["category"]}')


while True:
    print('''
food Database
1 Display Price
2 Update Stock
3 Display All
9 Quit''')
    choice = input('> ')
    if choice == '1':
        display_price(stocked_items)
    elif choice == '2':
        update_stock(stocked_items)
    elif choice == '3':
        display_all(stocked_items)
    elif choice == '9':
        break
    else:
        print('Invalid choice')















