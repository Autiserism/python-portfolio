def lose_life():
    global lives
    life_left = lives - 1
    lives = lives - 1
    print(life_left)
lives = 3
lose_life()
lose_life()

def greet(name):
    print('Welcome ' + name)
    return name

print('what is your name')
name = input('>')
greet(name)


def is_even(number):
    result = number % 2
    if result == 0 :
       return True
    else:
        return False
is_even(7)


