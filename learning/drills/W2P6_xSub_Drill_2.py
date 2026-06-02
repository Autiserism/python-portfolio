'''
 Index based loop to update a list
Write a function called replace_at that takes a list, a target value and a replacement value.
Loops through using range(len()) and replaces every occurrence of the target with the replacement.
Test it with three different lists.
'''


llist1 = 'mississippi'
llist2 = 'snakes'
llist3 = 'sossoessr'
llist5 = []
TV = 's'
RPV = '2'



def replace_at(llist5, TV, RPV):
    for i in range(len(llist3)):
        llist5.append(llist3[i])
        if llist5[i] == TV:
            llist5[i] = RPV
        continue
    return llist5

result = replace_at(llist5, TV, RPV)
print(result)





















