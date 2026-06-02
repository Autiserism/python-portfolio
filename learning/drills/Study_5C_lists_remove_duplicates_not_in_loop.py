# Write a function called remove_duplicates
# that takes a list and returns a new list with all duplicates removed
# keeping only the first occurrence of each item.
# Test it with: items = [1, 3, 2, 1, 5, 3, 4, 2, 6]
# Hint — you'll need an empty list to build into and check if an item is already in it using in.

items = [1, 3, 2, 1, 5, 3, 4, 2, 6]

def remove_duplicates(items):
    sorted_items = []
    for number in items:
        if number not in sorted_items:
            sorted_items.append(number)
    return sorted_items
new_items = remove_duplicates(items)
print (new_items)

