#Build an inventory system with a menu loop.
#Options: add item with quantity, restock item, sell item, view inventory, quit.
#Track quantities in a dictionary and warn when stock is below 5.

# define add_item(store_inv)
#     name = input.title()
#     if name in store_inv print exists, ask restock, call restock if yes, return
#     quantity = int input
#     if quantity < 1 print invalid, return
#     store_inv[name] = quantity
#     print confirmation

# define restock_item(store_inv)
#     view_inventory(store_inv)
#     name = input which item.title()
#     if name not in store_inv print not found, return
#     amount = int input how many to add
#     if amount < 1 print invalid, return
#     store_inv[name] += amount
#     print updated quantity

# define sell_item(store_inv)
#     view_inventory(store_inv)
#     name = input which item.title()
#     if name not in store_inv print not found, return
#     amount = int input how many sold
#     if amount < 1 print invalid, return
#     if amount > store_inv[name] print not enough stock, return
#     store_inv[name] -= amount
#     if store_inv[name] == 0 ask to remove, del if yes
#     print updated quantity
#     if store_inv[name] <= 4 print low stock warning

# define view_inventory(store_inv)
#     if not store_inv print empty
#     else for item, quantity in store_inv.items()
#         if quantity <= 4 print item + quantity + LOW STOCK WARNING
#         else print item + quantity

# store_inv = {}
# while True
#     print menu options
#     get choice
#     call matching function or break



def add_item(store_inv):
    name = input('Enter an item: ').title()
    if name in store_inv:
        print('already in inventory')
        if input('restock item?: yes or no ') == 'yes':
            restock_item(store_inv)
            return
    quantity = int(input('enter the quantity: '))
    if quantity < 1:
        print ('invalid')
        return
    store_inv[name] = quantity
    print (f"{quantity} {name} added")

def restock_item(store_inv):
    view_inventory(store_inv)
    name = input('which item?: ').title()
    if name not in store_inv:
        print ('not found: ')
        return
    amount = int(input('How many to add?: '))
    if amount < 1:
        print('invalid amount')
        return
    store_inv[name] += amount
    print (f'{name} + {amount} updated')


def sell_item(store_inv):
    view_inventory(store_inv)
    name = input('which item: ').title()
    if name not in store_inv:
        print('not found')
        return
    amount = int(input('enter amount sold: '))
    if amount < 1:
        print ('invalid')
        return
    if amount > store_inv[name]:
        print('not enough stock')
        return
    store_inv[name] -= amount
    if store_inv[name] == 0:
        if input('Remove item? yes or no: ') == 'yes':
            del store_inv[name]
            return  # add this - exit before the low stock check
    if store_inv[name] <= 4:
        print('low stock warning!')


def view_inventory(store_inv):
    if not store_inv:
        print('empty')
    else:
        for item, quantity in store_inv.items():
            if quantity <= 4:
                print(f'{item}: {quantity} LOW STOCK WARNING!')
            else:
                print(f'{item}: {quantity}')

store_inv = {'Apples': 10, 'Milk': 5}
while True:
    print("""\nStore Options
1 Add Item
2 Restock Item
3 Sell Item
4 View inventory
9 To Quit\n""")
    try:
        choice = int(input("Choose: "))
    except ValueError:
        print('Enter a valid number')
        continue
    if choice == 1:
        add_item(store_inv)
    elif choice == 2:
        restock_item(store_inv)
    elif choice == 3:
        sell_item(store_inv)
    elif choice == 4:
        view_inventory(store_inv)
    elif choice == 9:
        break
    else:
        print('Enter a valid input')




















