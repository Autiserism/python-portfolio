def full_name(first, last):
    return first + ' ' + last

print (full_name('Tylher', 'Girard'))


def check_password(password):
    if password == 'python123' :
        return 'Access Granted'
    else:
        return 'Acces denied'
print('whats the password')
password = input('>')
print(check_password(password))


def add_points():
    global score
    score = score + 5
def reset_score():
    global score
    score = 0
score = 0
add_points()
add_points()
add_points()
print(score)
reset_score()
print(score)





