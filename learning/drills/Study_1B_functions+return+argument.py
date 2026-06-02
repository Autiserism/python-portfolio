#Write a function called is_adult that takes an age as an argument and returns "Adult"
#if 18 or older, otherwise returns "Minor". Print the result.
def is_adult (age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
result = is_adult(18)
print(result)

