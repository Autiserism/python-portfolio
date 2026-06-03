'''
Build a shopping list program with a menu loop.
Options: add item, remove item, view list, quit.
Use a list to store items.
'''
# define add_item(list) - append item, print confirmation
# define remove_item(list) - check if exists, remove or print error
# define view_list(list) - check if empty, print accordingly
# create empty shopping list
# while True loop
#   print menu options
#   get choice, convert to lowercase
#   if add call add_item
#   elif remove call remove_item
#   elif view call view_list
#   elif quit break
#   else print invalid option


def add_item(S_List):
    item = input('add item: ').lower()
    if item not in S_List:
        S_List.append(item)
        print(f'{item} added.')    # confirmation
    else:
        print('That item is already in the list')

def remove_item(S_List):
    print(S_List)
    item = input('what item to remove?: ').lower()
    if item in S_List:
       S_List.remove(item)
    else:
        print('error item not found')

def view_list(S_List):
    if not S_List:
        print('Shoping list is empty!')
    else:
        print(S_List)


S_List = []

while True:
    print("""\nShopping List Would you Like too
1 Add an item
2 Remove an item
3 View list
9 To Quit\n""")
    choice = int(input("Choose: "))
    if choice == 1:
        add_item(S_List)
    elif choice == 2:
        remove_item(S_List)
    elif choice == 3:
        view_list(S_List)
    elif choice == 9:
        break
    else:
        print('Enter a valid input')





















