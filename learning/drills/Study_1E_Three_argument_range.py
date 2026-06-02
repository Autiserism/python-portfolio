#Write a function called clamp that takes three arguments — number, minimum, and maximum
#It should return minimum if the number is below the minimum,
#maximum if the number is above the maximum
# and the number itself if it's within range.
def clamp(number, minimum, maximum):
    if number < minimum:
        return minimum
    elif number > maximum:
        return maximum
    else:
        return number
print(clamp(50, 0, 100))
print(clamp(-5, 0, 100))
print(clamp(150, 0, 100))

