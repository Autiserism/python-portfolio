# Write a program that: Has a list of student names and a list of their scores
# Uses zip() to pair them together — zip(names, scores) combines two lists item by item
# Loops through the pairs and prints each student's name and score
# Finds and prints the highest scoring student using the logic from Drill 5B
# Test it with:
# names = ["Tyler", "Bob", "Sarah", "Mike", "Jess"]
# scores = [85, 92, 78, 95, 88]


names = ["Tyler", "Bob", "Sarah", "Mike", "Jess"]
scores = [85, 92, 78, 95, 88]

def higest_score(names, scores):
    best_name = names[0]
    best_score = scores[0]
    for name, score in zip(names, scores):
        print(name, score)
        if score > best_score:
            best_score = score
            best_name = name
    return best_name, best_score
result = higest_score(names, scores)
print(result)
