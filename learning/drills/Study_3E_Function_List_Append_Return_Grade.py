# Write a function called grade_list that takes a list of scores, loops through them
# and returns a new list with the letter grade for each score using this scale
# 90 or above → "A", 70 or above → "B", 50 or above → "C", below 50 → "F"
# Print the result.
# Test it with: scores = [95, 82, 55, 40, 73, 90, 61]
# Hint — you'll need to build a new list inside the function.
# You can add items to a list with .append():
# results = []           # empty list
# results.append("A")   # adds "A" to the list

scores = [95, 82, 55, 40, 73, 90, 61]
def grade_list (scores):
    results = []
    for mark in scores:
        if mark >= 90:
            results.append('A')
        elif mark >= 70:
            results.append('B')
        elif mark >= 50:
            results.append('C')
        else:
            results.append('F')
    return results
grades = grade_list(scores)
print(grades)
