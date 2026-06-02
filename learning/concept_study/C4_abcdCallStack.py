def a():
    print('a() starts')
    b() #1
    d() #2
    print('a() returns')

def b():
    print('b() starts')
    c() #3
    print('b() returns')

def c():
    print('c() starts') #4
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')
a() #5
