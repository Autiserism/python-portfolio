#Write a function called is_divisible that takes two numbers
#and returns True if the first is evenly divisible by the second
# otherwise returns False. Print the result.
def is_divisable(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
result= is_divisable(10 , 5)
print(result)
