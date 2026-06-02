# Write a program that creates a list of 5 of your favorite foods, then:
# Prints the first and last item using indexing
# Prints the first three items using slicing
# Adds a new food to the end
# Removes the second item
# Prints the final list

foods = ['steak','taco','omelette','pizza','soup']
print (foods[0])
print (foods[-1])
print (foods[0:3])

foods.append('pancakes')
foods.remove('taco')
print (foods)
