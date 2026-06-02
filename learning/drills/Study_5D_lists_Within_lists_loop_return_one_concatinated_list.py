# Write a function called flatten
# that takes a list of lists and returns a single flat list with all the items combined.
# Test it with: nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Hint — you'll need a loop inside a loop. The outer loop goes through each sublist,
# the inner loop goes through each item in that sublist.

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

def flatten(nested):
    big_list = []
    for list1 in nested:
        for item in list1:
            big_list.append(item)
    return big_list
result = flatten(nested)
print(result)
