'''
List comprehension practice
Rewrite these four loops as list comprehensions:
# Loop 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# Loop 2
words = ['hello', 'world', 'python', 'code']
upper = []
for word in words:
    upper.append(word.upper())

# Loop 3
scores = [45, 72, 88, 35, 91, 60]
passing = []
for score in scores:
    if score >= 60:
        passing.append(score)

# Loop 4
pairs = [('Tyler', 92), ('Bob', 65), ('Sarah', 78)]
names = []
for name, score in pairs:
    if score >= 70:
        names.append(name)
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [n for n in numbers if n % 2 == 0]
print(even)

words = ['hello', 'world', 'python', 'code']
upper = [word.upper() for word in words]
print(upper)

scores = [45, 72, 88, 35, 91, 60]
passing = [score for score in scores if score >= 60]
print(passing)

pairs = [('Gman', 92), ('Bob', 65), ('Sarah', 78)]
names = [name for name, score in pairs if score >= 70]
print(names)
































































