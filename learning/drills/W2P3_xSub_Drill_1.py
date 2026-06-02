'''
set() practice

Write a function that takes two lists and returns three things —
items only in list 1, items only in list 2, items in both.
Use set() operations.
'''

def use_set (list1, list2):
    only_in_1 = set(list1) - set(list2)
    only_in_2 = set(list2) - set(list1)
    in_both = set(list1) & set(list2)
    return only_in_1, only_in_2, in_both

list1 = [ 'the', 'dog','jumped','over', 'the','cat']
list2 = ['the','cat','ran','away','from','the','dog']

l1, l2, l3 = use_set(list1, list2)

print(f'list one items{l1},\nList 2 items{l2},\nConcatenate items{l3}')


'''
set1 - set2   # items only in set1
set2 - set1   # items only in set2
set1 & set2   # items in both
'''








